# -*- coding: utf-8 -*-
from odoo import http

# class ThDebtNoteOriginAr(http.Controller):
#     @http.route('/th_debt_note_origin_ar/th_debt_note_origin_ar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/th_debt_note_origin_ar/th_debt_note_origin_ar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('th_debt_note_origin_ar.listing', {
#             'root': '/th_debt_note_origin_ar/th_debt_note_origin_ar',
#             'objects': http.request.env['th_debt_note_origin_ar.th_debt_note_origin_ar'].search([]),
#         })

#     @http.route('/th_debt_note_origin_ar/th_debt_note_origin_ar/objects/<model("th_debt_note_origin_ar.th_debt_note_origin_ar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('th_debt_note_origin_ar.object', {
#             'object': obj
#         })