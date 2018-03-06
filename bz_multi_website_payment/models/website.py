# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Website(models.Model):
    _inherit = 'website'

    @api.model
    def payment_icons(self):
        '''
        Filter payment icons by website.
        '''
        res = super(Website, self).payment_icons()
        return self.env['payment.icon'].sudo().search([('id','in',res.ids),'|',('website_ids','in',self.env['website'].get_current_website().id),('website_ids','=',False)])