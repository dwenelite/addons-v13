# -*- coding: utf-8 -*-
# from odoo import http


# class Yuhu(http.Controller):
#     @http.route('/yuhu/yuhu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yuhu/yuhu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yuhu.listing', {
#             'root': '/yuhu/yuhu',
#             'objects': http.request.env['yuhu.yuhu'].search([]),
#         })

#     @http.route('/yuhu/yuhu/objects/<model("yuhu.yuhu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yuhu.object', {
#             'object': obj
#         })
