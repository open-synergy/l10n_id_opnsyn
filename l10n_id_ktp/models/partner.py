# -*- encoding: utf-8 -*-
##############################################################################
#    Author : Andhitia Rama, Michael Viriyananda, Nurazmi
#    Copyright (C) 2015 OpenSynergy Indonesia
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import fields, models


class Partner(models.Model):
    """Partners with gender."""
    _inherit = "res.partner"

    ktp = fields.Char(string='KTP')
    ktp_expired_date = fields.Date(string='KTP Expired Date')
