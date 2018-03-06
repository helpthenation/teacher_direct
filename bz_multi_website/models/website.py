# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Website(models.Model):
    _inherit = 'website'

    def _get_page_count(self):
        '''
        Get the number of pages related to the website.
        '''
        websitePageObj = self.env['website.page']
        for website in self:
            website.page_count = websitePageObj.search_count([('website_ids','in',website.id)])

    def _get_menu_count(self):
        '''
        Get the number of menu related to the website.
        '''
        websiteMenuObj = self.env['website.menu']
        for website in self:
            website.menu_count = websiteMenuObj.search_count([('website_id','=',website.id)])

    page_count = fields.Integer('Page Count', compute='_get_page_count')
    menu_count = fields.Integer('Menu Count', compute='_get_menu_count')
    template_user_id = fields.Many2one('res.users', 'Template User')
    auth_signup_uninvited = fields.Boolean('Allow Sign-up')
    auth_signup_reset_password = fields.Boolean('Allow Password Reset')
    theme_id = fields.Many2one('ir.module.module')
    canonical_website = fields.Many2one('website', 'Canonical Website')

    @api.model
    def create(self, vals):
        '''
        Create top menu when creating a new website.
        '''
        res = super(Website, self).create(vals)
        self.env['website.menu'].create({
            'name': 'Top Menu - {0}'.format(res.name),
            'website_id': res.id
        })
        return res