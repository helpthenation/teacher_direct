# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.http_routing.models.ir_http import slug

class WebsiteSale(WebsiteSale):

    @http.route()
    def product(self, product, category='', search='', **kwargs):
        '''
        Add the product canonical url to the page.
        '''
        res = super(WebsiteSale, self).product(product, category, search, **kwargs)
        if request.website and request.website.canonical_website:
            canonical_url = '{0}://{1}/shop/product/{2}'.format(request.httprequest.environ.get('wsgi.url_scheme', 'http'), request.website.canonical_website.domain, slug(product))
        else:
            canonical_url = '{0}://{1}/shop/product/{2}'.format(request.httprequest.environ.get('wsgi.url_scheme', 'http'), request.website.domain, slug(product))
        res.qcontext.update({'canonical_url': canonical_url})
        return res
