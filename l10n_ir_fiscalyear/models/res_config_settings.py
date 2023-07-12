# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_ir_fiscalyear_last_month = fields.Selection(related='company_id.l10n_ir_fiscalyear_last_month', readonly=False)
    l10n_ir_fiscalyear_last_day = fields.Integer(related='company_id.l10n_ir_fiscalyear_last_day', readonly=False)
