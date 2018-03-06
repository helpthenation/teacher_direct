# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    website_ids = fields.Many2many('website', string='Websites')