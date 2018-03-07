# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'


    def _compute_quantities_dict(self, lot_id, owner_id, package_id, from_date=False, to_date=False):
        '''
        Get quantity based on current website warehouse
        '''
        website = self.env['website'].get_current_website()
        if website.warehouse_id:
            res = super(ProductProduct, self.with_context(warehouse=website.warehouse_id.id))._compute_quantities_dict(lot_id, owner_id, package_id, from_date, to_date)
        else:
            res = super(ProductProduct, self)._compute_quantities_dict(lot_id, owner_id, package_id, from_date, to_date)
        return res
