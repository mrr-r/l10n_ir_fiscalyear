# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import date,datetime
import jdatetime as jd
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Company(models.Model):
    _inherit = "res.company"
    _check_company_auto = True

    l10n_ir_fiscalyear_last_month = fields.Selection([
        ('1', 'Farvardin'),
        ('2', 'Ordibehesht'),
        ('3', 'Khordad'),
        ('4', 'Tir'),
        ('5', 'Mordad'),
        ('6', 'Shahrivar'),
        ('7', 'Mehr'),
        ('8', 'Aban'),
        ('9', 'Azar'),
        ('10', 'Dey'),
        ('11', 'Bahman'),
        ('12', 'Esfand'),
    ], default='12', inverse='_inverse_selection')

    l10n_ir_fiscalyear_last_day = fields.Integer(default=30, inverse='_inverse_selection')

    @api.depends('l10n_ir_fiscalyear_last_month', 'l10n_ir_fiscalyear_last_day')
    def _inverse_selection(self):
        for rec in self:
            try:
                # TODO FIX 2020 with this year 
                if rec.l10n_ir_fiscalyear_last_month and rec.l10n_ir_fiscalyear_last_day:
                    just_jdate_str = jd.date(day=rec.l10n_ir_fiscalyear_last_day, month=int(rec.l10n_ir_fiscalyear_last_month), year=2020, locale="fa_IR")
                    date = jd.date.togregorian(just_jdate_str).strftime("%Y-%m-%d")
                    date = datetime.strptime(date, '%Y-%m-%d')
                    self.env.company.write({
                            'fiscalyear_last_day': date.day or self.env.company.fiscalyear_last_day,
                            'fiscalyear_last_month': str(date.month) or self.env.company.fiscalyear_last_month,
                            })
            except Exception as e:
                raise ValidationError(
                    _('fiscal year last day: day is out of range for month. Month: %s; Day: %s') %
                    (rec.l10n_ir_fiscalyear_last_month, rec.l10n_ir_fiscalyear_last_day)
                )
        
    