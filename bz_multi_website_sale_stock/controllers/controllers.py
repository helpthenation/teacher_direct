# -*- coding: utf-8 -*-
from odoo import http

# class BzMultiWebsiteSaleStock(http.Controller):
#     @http.route('/bz_multi_website_sale_stock/bz_multi_website_sale_stock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bz_multi_website_sale_stock/bz_multi_website_sale_stock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bz_multi_website_sale_stock.listing', {
#             'root': '/bz_multi_website_sale_stock/bz_multi_website_sale_stock',
#             'objects': http.request.env['bz_multi_website_sale_stock.bz_multi_website_sale_stock'].search([]),
#         })

#     @http.route('/bz_multi_website_sale_stock/bz_multi_website_sale_stock/objects/<model("bz_multi_website_sale_stock.bz_multi_website_sale_stock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bz_multi_website_sale_stock.object', {
#             'object': obj
#         })