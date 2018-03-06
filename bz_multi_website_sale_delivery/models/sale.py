# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_delivery_methods(self):
        '''
        Filter delivery methods by website.
        '''
        res = super(SaleOrder, self)._get_delivery_methods()
        return self.env['delivery.carrier'].sudo().search([('id','in',res.ids),'|',('website_ids','in',self.env['website'].get_current_website().id),('website_ids','=',False)])