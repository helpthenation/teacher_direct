# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IrUiView(models.Model):
    _inherit = 'ir.ui.view'

    @api.multi
    def toggle(self):
        '''
        Toggle custom views based on website.
        '''
        for view in self:
            website_id = self.env['website'].get_current_website().id
            website_view = self.with_context(active_test=False).search([('key','=',view.key),('website_id','=',website_id)])
            if not website_view:
                website_view = view.copy({'website_id': website_id})
            website_view.write({'active': not view.active})

    @api.model
    def get_related_views(self, key, bundles=False):
        '''
        Filter views by website.
        '''
        res = super(IrUiView, self).get_related_views(key, bundles=bundles)
        views = self.env['ir.ui.view']
        for view in res:
            if (not view.website_id and self.with_context(active_test=False).search([('id','!=',view.id),('website_id','=',self.env.context.get('website_id')),('key','=',view.key)])) or (view.website_id and view.website_id.id != self.env.context.get('website_id')):
                continue
            views += view
        return views

    @api.model
    def get_inheriting_views_arch(self, view_id, model):
        '''
        Filter views based on website.api
        '''
        arch = super(IrUiView, self).get_inheriting_views_arch(view_id, model)
        vw = self.browse(view_id)
        if (self.env.context and self.env.context.get('website_id') and vw.type == 'qweb'):
            old_arch = list(arch)
            for x, view_id in enumerate(old_arch):
                view = self.browse(view_id[1])
                if not view.website_id and self.with_context(active_test=False).search([('id','!=',view.id),('website_id','=',self.env.context.get('website_id')),('key','=',view.key)]):
                    arch.pop(x)
        return arch