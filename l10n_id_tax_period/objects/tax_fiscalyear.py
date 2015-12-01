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

class Fiscalyear(models.Model):
    _name = 'tax.fiscal_year'
    _description = 'Tax Fiscalyear'
    _columns = {
        'name': fields.char(
            string='Fiscalyear',
            size=30,
            required=True,
            ),
        'code': fields.char(
            string='Code',
            size=10,
            required=True,
            ),
        'date_start': fields.date(
            string='Date Start',
            required=True,
            ),
        'date_end': fields.date(
            string='Tanggal Akhir',
            required=True,
            ),
        'period_ids': fields.one2many(
            obj='tax.period',
            fields_id='tax_fiscalyear_id',
            string='Tax Period',
            ),
        }

Fiscalyear()
