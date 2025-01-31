# -*- coding: utf-8 -*-
# from odoo import http


# class Addonbaru(http.Controller):
#     @http.route('/addonbaru/addonbaru', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addonbaru/addonbaru/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addonbaru.listing', {
#             'root': '/addonbaru/addonbaru',
#             'objects': http.request.env['addonbaru.addonbaru'].search([]),
#         })

#     @http.route('/addonbaru/addonbaru/objects/<model("addonbaru.addonbaru"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addonbaru.object', {
#             'object': obj
#         })

