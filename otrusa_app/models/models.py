# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class sale_order_line(models.Model):
    _inherit= 'sale.order.line'

    x_stock_quant_app = fields.One2many('stock.quant','product_id',related='product_id.x_stock_quant')
    credit_limit_app = fields.Float('Credit Limit')
    credit_limit_on_hold  = fields.Boolean('Credit limit on hold')
