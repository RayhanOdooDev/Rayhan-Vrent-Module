# -*- coding: utf-8 -*-
# from odoo import http


# class Vrental(http.Controller):
#     @http.route('/vrental/vrental', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vrental/vrental/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vrental.listing', {
#             'root': '/vrental/vrental',
#             'objects': http.request.env['vrental.vrental'].search([]),
#         })

#     @http.route('/vrental/vrental/objects/<model("vrental.vrental"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vrental.object', {
#             'object': obj
#         })
