## begin license ##
#
# "Gustos" is a monitoring tool by Seecr. These are the open source parts used in different projects.
#
# Copyright (C) 2011-2014, 2018 Seecr (Seek You Too B.V.) https://seecr.nl
# Copyright (C) 2012 Stichting Bibliotheek.nl (BNL) http://www.bibliotheek.nl
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

from optparse import OptionParser, Option

from sys import exit

class ParseArguments(object):
    """Helper for OptionParser, more or less the same as meresco.components.ParseArguments
    To avoid dependency on meresco-components it is copied here."""
    def __init__(self):
        self._parser = OptionParser()
        self._mandatoryKeys = []
        self.print_help = self._parser.print_help

    def _parse(self, args=None):
        options, arguments = self._parser.parse_args(args)
        for key in self._mandatoryKeys:
            if getattr(options, key, None) == None:
                raise ValueError("Option '%s' is missing." % key)
        return options, arguments

    def addOption(self, *args, **kwargs):
        mandatory = kwargs.pop('mandatory', False)
        option = Option(*args, **kwargs)
        if mandatory:
            self._mandatoryKeys.append(option.dest)
        self._parser.add_option(option)

    def parse(self, args=None):
        try:
            return self._parse(args=args)
        except ValueError as e:
            print(('\033[1;31m%s\033[0m' % str(e)))
            self.print_help()
            exit(1)
