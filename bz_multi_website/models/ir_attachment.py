# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    website_id = fields.Many2one('website', 'Website')