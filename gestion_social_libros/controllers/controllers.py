# -*- coding: utf-8 -*-
from odoo import http

# class GestionSocialLibros(http.Controller):
#     @http.route('/gestion_social_libros/gestion_social_libros/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_social_libros/gestion_social_libros/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_social_libros.listing', {
#             'root': '/gestion_social_libros/gestion_social_libros',
#             'objects': http.request.env['gestion_social_libros.gestion_social_libros'].search([]),
#         })

#     @http.route('/gestion_social_libros/gestion_social_libros/objects/<model("gestion_social_libros.gestion_social_libros"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_social_libros.object', {
#             'object': obj
#         })