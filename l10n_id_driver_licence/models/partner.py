# -*- encoding: utf-8 -*-

# Odoo, Open Source Management Solution
# Copyright (C) 2014-2015  Grupo ESOC <www.grupoesoc.es>
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

from openerp import fields, models


class Partner(models.Model):
    """Partners with gender."""
    _inherit = "res.partner"

    sim_a = fields.Char(string='SIM A')
    sim_a_expired_date = fields.Date(string='SIM A Expired Date')
    sim_b1 = fields.Char(string='SIM B1')
    sim_b1_expired_date = fields.Date(string='SIM B1 Expired Date')
    sim_b2 = fields.Char(string='SIM B2')
    sim_b2_expired_date = fields.Date(string='SIM B2 Expired Date')
    sim_c = fields.Char(string='SIM C')
    sim_c_expired_date = fields.Date(string='SIM C Expired Date')
    sim_d = fields.Char(string='SIM D')
    sim_d_expired_date = fields.Date(string='SIM D Expired Date')
