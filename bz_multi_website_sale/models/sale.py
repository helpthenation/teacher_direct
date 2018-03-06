# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.multi
    def action_quotation_send(self):
        '''
        Send website specific email template if available.
        '''
        self.ensure_one()
        res = super(SaleOrder, self).action_quotation_send()
        template = self.env['website'].get_current_website().order_mail_template
        if template:
            res.get('context', {}).update({
                'default_use_template': bool(template.id),
                'default_template_id': template.id
            })
        return res