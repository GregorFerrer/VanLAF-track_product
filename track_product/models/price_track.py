from odoo import models, fields, api


class track_price_product(models.Model):
    _name = 'track.price.product'
    _description = 'track_product'

    name = fields.Char(string="description", store="True")
    product_tmpl = fields.Many2one("Product.template", string="product")
    pricelist_id = fields.Many2one("product.pricelist", string="pricelist", store="True")
    value = fields.Float(string="", store="True")
    load_date = fields.Datetime(string="Date", store="True")

    
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100