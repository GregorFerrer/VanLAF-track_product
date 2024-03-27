from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = "product.template" 
    
    
    lines_track_cost = fields.One2many('track.costproduct', 'product_tmpl', string="Lines cost" , store="True")
    lines_track_price = fields.One2many('track.priceproduct', 'product_tmpl', string="Lines price" , store="True")
    
