# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website

class Website(Website):

    @http.route()
    def theme_customize_get(self, xml_ids):
        '''
        Override function to use keys instead of xml_id
        '''
        enable = []
        disable = []
        ids = self.get_view_ids(xml_ids)
        for view in request.env['ir.ui.view'].with_context(active_test=True).browse(ids):
            if view.active:
                enable.append(view.key)
            else:
                disable.append(view.key)
        return [enable, disable]

    @http.route()
    def theme_customize(self, enable, disable, get_bundle=False):
        """
        Override function to set view per website.
        """
        def set_active(ids, active):
            if ids:
                if active == True:
                    real_ids = self.get_view_ids(ids)
                    for view in request.env['ir.ui.view'].with_context(active_test=True).browse(real_ids):
                        if not view.website_id:
                            view.copy({'website_id': request.website.id})
                real_ids = self.get_view_ids(ids)
                request.env['ir.ui.view'].with_context(active_test=True).browse(real_ids).write({'active': active})
        set_active(disable, False)
        set_active(enable, True)
        if get_bundle:
            context = dict(request.context, active_test=True)
            return request.env["ir.qweb"]._get_asset('web.assets_frontend', options=context)
        return True