# © 2019 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    retail_model = fields.Char('Model')
    retail_series = fields.Char('Series')
    retail_colour = fields.Char('Colour')
    retail_sequence = fields.Char('Sequence')
