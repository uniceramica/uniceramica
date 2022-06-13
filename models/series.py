from odoo import models,fields,api

class ProductSeries(models.Model):
    _inherit = 'product.template'
    series_ids = fields.Many2many("product.series",string="Series" )
    series_count = fields.Integer(string='Series Count',compute='_compute_count_series')

    @api.depends('series_ids')
    def _compute_count_series(self):
        for p in self:
                p.series_count = len(p.series_ids)

class SeriesProduct(models.Model):
    _name = 'product.series'
    _description = "Series"

    name= fields.Char(string="Name")
    #series_image = fields.Binary()
    product_ids = fields.Many2many("product.template",string="Products")
'''
    product_count = fields.Integer(string='Product Count',compute='_compute_count_products')

    @api.depends('product_ids')
    def _compute_count_product(self):
        for p in self:
                p.product_count = len(p.product_ids)
'''
'''
class BrandPivot(models.Model):
    _inherit = 'sale.report'

    brand_id=fields.Many2one ('product.brand' ,string='Brand')

    def _query(self):
        res= super(BrandPivot, self)._query()
        query = res.split('t.categ_id as categ_id,',1)
        query= query[0]+'t.categ_id as categ_id,t.brand_id as brand_id,' +query[1]
        split= query.split('t.categ_id,',1)
        res = split[0] + 't.categ_id,t.brand_id,' + split[1]
        return res
'''