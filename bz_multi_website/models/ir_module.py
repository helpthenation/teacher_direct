# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    @api.depends('website_ids')
    def _get_current_theme(self):
        '''
        Get wheter the theme is installed for the current website.
        '''
        for module in self:
            if self.env.context.get('active_model', '') == 'website':
                website_id = self.env.context.get('active_id')
            else:
                website_id = self.env['website'].get_current_website().id
            if website_id in module.website_ids.ids:
                module.current_theme = True
            else:
                module.current_theme = False

    website_ids = fields.One2many('website', 'theme_id', string='Websites')
    current_theme = fields.Boolean('Current Theme', compute='_get_current_theme')

    @api.multi
    def button_choose_theme(self):
        '''
        Over ride function to set the theme that the website is using.
        '''
        if self.env.context.get('active_model', False) == 'website':
            website = self.env['website'].browse(self.env.context.get('active_id', 1))
            website.write({'theme_id': self.id})
            theme_category = self.env.ref('base.module_category_theme', False)
            hidden_category = self.env.ref('base.module_category_hidden', False)
            theme_hidden_category = self.env.ref('base.module_category_theme_hidden', False)
            theme_category_id = theme_category.id if theme_category else 0
            hidden_categories_ids = [hidden_category.id if hidden_category else 0, theme_hidden_category.id if theme_hidden_category else 0]
            #If not used on other websites uninstall
            self.with_context(theme_website_id=website.id).search([ # Uninstall the theme(s) which is (are) installed
                ('state', '=', 'installed'), ('website_ids','=',False),
                '|', ('category_id', 'not in', hidden_categories_ids), ('name', '=', 'theme_default'),
                '|', ('category_id', '=', theme_category_id), ('category_id.parent_id', '=', theme_category_id)
            ]).button_immediate_uninstall()
            #If used on other websites just delete this websites views
            self.search([ # Uninstall the theme(s) which is (are) installed
                ('state', '=', 'installed'), ('website_ids','not in',website.id), ('website_ids','!=',False),
                '|', ('category_id', 'not in', hidden_categories_ids), ('name', '=', 'theme_default'),
                '|', ('category_id', '=', theme_category_id), ('category_id.parent_id', '=', theme_category_id)
            ]).remove_website_views(website)
            if self.state == 'installed':
                next_action = self.with_context(theme_website_id=website.id).button_immediate_upgrade() # Then upgrade the new chosen one
            else:
                next_action = self.with_context(theme_website_id=website.id).button_immediate_install() # Then install the new chosen one
            if next_action.get('tag') == 'reload' and not next_action.get('params', {}).get('menu_id'):
                next_action = self.env.ref('website.action_website').read()[0]
            return next_action
        return super(IrModuleModule, self).button_choose_theme()

    @api.multi
    def _button_immediate_function(self, function):
        '''
        Delete views when a module is uninstalled and create new views when 
        installed or upgraded.
        '''
        viewObj = self.env['ir.ui.view']
        if self.env.context.get('theme_website_id', False):
            #Remove existing website views for uninstall
            if function.__name__ == 'button_uninstall':
                for module in self:
                    for website in self.env['website'].search([]):
                        self.remove_website_views(website)
        res = super(IrModuleModule, self)._button_immediate_function(function)
        if self.env.context.get('theme_website_id', False):
            #Add new views for install
            if function.__name__ in ['button_install','button_upgrade']:
                website = self.env['website'].browse(self.env.context['theme_website_id'])
                for module in self:
                    if module.website_ids:
                        model_data = self.env['ir.model.data'].search([('module','=',module.name), ('model','=','ir.ui.view')])
                        views = viewObj.browse([data['res_id'] for data in model_data])
                        views_unlink = viewObj
                        for view in views:
                            if view.key and '.s_' not in view.key:
                                view.copy({'website_id': website.id})
                                views_unlink += view
                        views_unlink.unlink()
        return res

    @api.multi
    def remove_website_views(self, website):
        '''
        Delete website specific views for a module.
        '''
        viewObj = self.env['ir.ui.view']
        for module in self:
            viewObj.with_context(active_test=False).search([('key','=ilike',module.name+'.%'),('website_id','=',website.id)]).unlink()