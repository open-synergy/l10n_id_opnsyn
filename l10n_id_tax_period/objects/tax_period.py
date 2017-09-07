# -*- coding: utf-8 -*-
#    Author : Andhitia Rama, Michael Viriyananda, Nurazmi
#    Copyright (C) 2015 OpenSynergy Indonesia

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields


class TaxPeriod(models.Model):
    _name = 'tax.period'
    _description = 'Tax Period'

    name = fields.Char(
        string='Tax Period',
        size=30,
        required=True,
        )
    code = fields.Char(
        string='Code',
        size=30,
        required=True,
        )
    tax_fiscalyear_id = fields.Many2one(
        comodel_name='tax.fiscalyear',
        string='Tax Fiscalyear',
        required=True,
        )
    date_start = fields.Date(
        string='Date start',
        required=True,
        )
    date_end = fields.Date(
        string='Date End',
        required=True,
        )
    sequence = fields.Integer(
        string='Sequence',
        )
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('open', 'Open'),
            ('close', 'Closed')
            ],
        string='Status',
        readonly=True,
        )
    company_id = fields.Related(
        'tax_fiscalyear_id',
        'company_id',
        type='many2one',
        comodel_name='res.company',
        store=True,
        )
