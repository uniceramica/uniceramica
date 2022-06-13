###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import models,fields

class ProductCategory(models.Model):
    _inherit = 'product.category'
    
    sequence = fields.Integer(string='Category Sequence', Index=True)

    _order = "sequence, name"