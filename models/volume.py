# -*- coding: utf-8 -*-
##################
#
#   Uniceramica.it
#
##################

from odoo import api, models, fields


class ProductDimensionsVolume(models.Model):
    _inherit = 'product.template'

    length = fields.Float(string="Length", digits=(3, 7))
    breadth = fields.Float(string="Breadth", digits=(3, 7))
    height = fields.Float(string="Height", digits=(3, 7))

    package_length = fields.Float(string="Package Length", digits=(3, 7))
    package_breadth = fields.Float(string="Package Breadth", digits=(3, 7))
    package_height = fields.Float(string="Package Height", digits=(3, 7))
    package_volume = fields.Float(string="Package Volume", digits=(3, 7))

    @api.onchange('length', 'breadth', 'height')
    def onchange_l_b_h(self):
        self.volume = float(self.length if self.length else 0) * float(self.breadth if self.breadth else 0) * float(
            self.height if self.height else 0)

    @api.onchange('package_length', 'package_breadth', 'package_height')
    def package_onchange_l_b_h(self):
        self.package_volume = float(self.package_length if self.package_length else 0) * float(self.package_breadth if self.package_breadth else 0) * float(
            self.package_height if self.package_height else 0)

