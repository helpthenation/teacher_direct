# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Website(models.Model):
    _inherit = 'website'

    automatic_invoice = fields.Boolean('Automatic Invoice')
    cart_recovery_mail_template = fields.Many2one('mail.template', 'Cart Recovery Mail')
    cart_abandoned_delay = fields.Float('Abandoned Delay', default=1.0)
    order_mail_template = fields.Many2one('mail.template', 'Sale Order Mail')
