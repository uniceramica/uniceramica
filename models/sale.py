# -*- coding: utf-8 -*-
##################
#
#   Uniceramica.it
#
##################

from odoo import api, models, fields


class Sale(models.Model):
    _inherit = 'sale.order.line'

    is_on_offer = fields.Boolean(string='Is On Offer')
    disc_price = fields.Float(string='Unit Price After Discount', compute='_compute_details')
    price_subtotal_untaxed = fields.Float(string='Sub Total Untaxed', compute='_compute_details')

    @api.depends('price_unit','product_uom_qty', 'discount', 'tax_id')
    def _compute_details(self):
        for line in self:
            line.disc_price = line.price_unit - (line.price_unit * line.discount / 100)
            line.price_subtotal_untaxed = line.price_subtotal