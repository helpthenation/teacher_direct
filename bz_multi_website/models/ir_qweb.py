# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from odoo.addons.base.ir.ir_qweb.qweb import QWeb
from .assets_bundle import AssetsBundle

class IrQWeb(models.AbstractModel, QWeb):
    _inherit = 'ir.qweb'

    @tools.conditional(
        'xml' not in tools.config['dev_mode'],
        tools.ormcache_context('xmlid', 'options.get("lang", "en_US")', 'css', 'js', 'debug', 'async', keys=("website_id",)),
    )
    def _get_asset(self, xmlid, options, css=True, js=True, debug=False, async=False, values=None):
        '''
        Override function to use new assets bundle function.
        '''
        files, remains = self._get_asset_content(xmlid, options)
        asset = AssetsBundle(xmlid, files, remains, env=self.env)
        return asset.to_html(css=css, js=js, debug=debug, async=async, url_for=(values or {}).get('url_for', lambda url: url))