# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def _get_param(self, key):
        '''
        Make parameters website specific.
        '''
        if key == 'website_sale.automatic_invoice':
            return str(self.env['website'].get_current_website().automatic_invoice)
        elif key == 'website_sale.cart_recovery_mail_template_id':
            return str(self.env['website'].get_current_website().cart_recovery_mail_template.id)
        elif key == 'website_sale.cart_abandoned_delay':
            return str(self.env['website'].get_current_website().cart_abandoned_delay)
        return super(IrConfigParameter, self)._get_param(key)