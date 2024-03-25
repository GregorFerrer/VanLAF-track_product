from odoo import models, fields, api


class TrackCostProduct(models.Model):
    _name = "track.costproduct"

    name = fields.Char(string="description", store="True")
    product_tmpl = fields.Many2one("product.template", string="Product")
    value = fields.Float(string="Cost", store="True")

    def create(self, vals):
        record = super(TrackCostProduct, self).create(vals)
        record['name'] = 'RECORD' + '-' + str(record.id)

        return record