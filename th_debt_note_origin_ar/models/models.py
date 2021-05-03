# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class th_debt_note_origin_ar(models.Model):
#     _name = 'th_debt_note_origin_ar.th_debt_note_origin_ar'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100