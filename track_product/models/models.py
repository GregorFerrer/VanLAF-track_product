# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class track_product(models.Model):
#     _name = 'track_product.track_product'
#     _description = 'track_product.track_product'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
