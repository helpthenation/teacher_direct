# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Website(models.Model):
    _inherit = 'website'

    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse')