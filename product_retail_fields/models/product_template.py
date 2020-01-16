# © 2020 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    retail_model = fields.Char('Model')
    retail_series = fields.Char('Series')
    retail_colour = fields.Char('Colour')
    retail_sequence = fields.Char('Sequence')
    retail_brand = fields.Char('Brand', index=True)
    retail_type = fields.Char('Type', index=True)
