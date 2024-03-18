# -*- coding: utf-8 -*-
# from odoo import http


# class TrackProduct(http.Controller):
#     @http.route('/track_product/track_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/track_product/track_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('track_product.listing', {
#             'root': '/track_product/track_product',
#             'objects': http.request.env['track_product.track_product'].search([]),
#         })

#     @http.route('/track_product/track_product/objects/<model("track_product.track_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('track_product.object', {
#             'object': obj
#         })
