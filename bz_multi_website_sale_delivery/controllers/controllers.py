# -*- coding: utf-8 -*-
from odoo import http

# class BzMultiWebsiteSaleDelivery(http.Controller):
#     @http.route('/bz_multi_website_sale_delivery/bz_multi_website_sale_delivery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bz_multi_website_sale_delivery/bz_multi_website_sale_delivery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bz_multi_website_sale_delivery.listing', {
#             'root': '/bz_multi_website_sale_delivery/bz_multi_website_sale_delivery',
#             'objects': http.request.env['bz_multi_website_sale_delivery.bz_multi_website_sale_delivery'].search([]),
#         })

#     @http.route('/bz_multi_website_sale_delivery/bz_multi_website_sale_delivery/objects/<model("bz_multi_website_sale_delivery.bz_multi_website_sale_delivery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bz_multi_website_sale_delivery.object', {
#             'object': obj
#         })