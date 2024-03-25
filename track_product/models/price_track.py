from odoo import models, fields, api


class TrackPriceProduct(models.Model):
    _name = 'track.priceproduct'

    name = fields.Char(string="description", store="True")
    product_tmpl = fields.Many2one("product.template", string="product")
    pricelist_id = fields.Many2one("product.pricelist", string="pricelist", store="True")
    value = fields.Float(string="Price", store="True")

    
    def create(self, vals):
        record = super(TrackPriceProduct, self).create(vals)
        record['name'] = 'RECORD' + '-' + str(record.id)

        return record
    
