## begin license ##
#
# "Gustos" is a monitoring tool by Seecr. These are the open source parts used in different projects.
#
# Copyright (C) 2012-2015, 2018 Seecr (Seek You Too B.V.) https://seecr.nl
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

from distutils.core import setup
from os import walk

version = '$Version: master$'[9:-1].strip()

packages = ['gustos']
for path, dirs, files in walk('gustos'):
    if '__init__.py' in files:
        packagename = path.replace('/', '.')
        packages.append(packagename)

setup(
    name='gustos-common',
    packages=packages,
    version=version,
    url='http://gustos.seecr.nl',
    author='Seecr (Seek You Too B.V.)',
    author_email='info@seecr.nl',
    description='Gustos monitoring tool (commons).',
    long_description='Gustos monitoring tool (commons).',
    license='GNU Public License',
    platforms='all',
)
