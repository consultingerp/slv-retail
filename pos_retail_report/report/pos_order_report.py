# © 2020 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models


class PosOrderReport(models.Model):
    _inherit = 'report.pos.order'

    retail_brand = fields.Char('Brand', readonly=True)
    retail_type = fields.Char('Type', readonly=True)

    def _select(self):
        return "%s, %s, %s" % (
            super()._select(),
            'pt.retail_brand AS retail_brand',
            'pt.retail_type AS retail_type')

    def _group_by(self):
        return "%s, %s, %s" % (
            super()._group_by(),
            'pt.retail_brand',
            'pt.retail_type')
