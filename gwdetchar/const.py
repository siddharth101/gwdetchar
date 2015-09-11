# coding=utf-8
# Copyright (C) Duncan Macleod (2015)
#
# This file is part of the GW DetChar python package.
#
# GW DetChar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GW DetChar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GW DetChar.  If not, see <http://www.gnu.org/licenses/>.

"""Constants for `gwdetchar`
"""

import os

IFO = os.getenv('IFO', None)
ifo = os.getenv('ifo', None)
SITE = os.getenv('SITE', None)
site = os.getenv('site', None)
O1_SEGMENT_SERVER = os.getenv('O1_SEGMENT_SERVER', 'https://segments.ligo.org')
S6_SEGMENT_SERVER = os.getenv('S6_SEGMENT_SERVER', 'https://segdb.ligo.caltech.edu')
