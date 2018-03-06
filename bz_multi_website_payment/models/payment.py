# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    website_ids = fields.Many2many('website', string='Websites')

class PaymentIcon(models.Model):
    _inherit = 'payment.icon'

    website_ids = fields.Many2many('website', string='Websites')