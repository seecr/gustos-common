#!/bin/bash
## begin license ##
#
# "Gustos" is a monitoring tool by Seecr. These are the open source parts used in different projects.
#
# Copyright (C) 2005-2010 Seek You Too B.V. (CQ2) http://www.cq2.nl
# Copyright (C) 2011-2014, 2018 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Gustos-Common"
#
# "Gustos-Common" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Gustos-Common" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Gustos-Common"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

set -o errexit
export LANG=en_US.UTF-8
export PYTHONPATH=.:$PYTHONPATH
python3 _alltests.py "$@"
