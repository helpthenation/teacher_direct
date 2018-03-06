# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSale(WebsiteSale):

    def _get_shop_payment_values(self, order, **kwargs):
        '''
        Filter payment acquirers by website.
        '''
        res = super(WebsiteSale, self)._get_shop_payment_values(order, **kwargs)
        if request.website:
            res['form_acquirers'] = [acq for acq in res['form_acquirers'] if request.website.id in acq.website_ids.ids or not acq.website_ids]
            res['s2s_acquirers'] = [acq for acq in res['s2s_acquirers'] if request.website.id in acq.website_ids.ids or not acq.website_ids]
        return res