# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class product(models.Model):
#     _name = 'product.product'
#     _description = 'product.product'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    slug = fields.Char(string='Slug', compute='_compute_slug', store=True)
    additional_barcode = fields.Char(string='Additional Barcode', unique=True)

    def _compute_slug(self):
        for product in self:
            product.slug = product.name.replace(' ', '-').lower()

    @api.constrains('additional_barcode')
    def _check_unique_additional_barcode(self):
        for product in self:
            if product.additional_barcode:
                if self.search([('id', '!=', product.id), ('additional_barcode', '=', product.additional_barcode)]):
                    raise exceptions.ValidationError("Additional barcode must be unique.")
