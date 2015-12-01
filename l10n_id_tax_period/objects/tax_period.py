# -*- coding: utf-8 -*-
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#
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

    def default_state(self, cr, uid, context={}):
        return 'draft'

    _columns = {
        'name': fields.char(
            string='Tax Period',
            size=30,
            required=True,
            ),
        'code': fields.char(
            string='Code',
            size=30,
            required=True,
            ),
        'tax_fiscalyear_id': fields.many2one(
            obj='tax.fiscal_year',
            string='Tax Fiscalyear',
            required=True,
            ),
        'date_start': fields.date(
            string='Date start',
            required=True,
            ),
        'date_end': fields.date(
            string='Date End',
            required=True,
            ),
        'sequence': fields.integer(
            string='Sequence',
            ),
        'state': fields.selection(
            selection=[
                ('draft', 'Draft'),
                ('open', 'Open'),
                ('close', 'Closed')
                ],
            string='Status',
            readonly=True,
            ),
        }

    _defaults = {
        'state': default_state,
        }

TaxPeriod()
