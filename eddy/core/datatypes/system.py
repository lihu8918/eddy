# -*- coding: utf-8 -*-

##########################################################################
#                                                                        #
#  Eddy: a graphical editor for the specification of Graphol ontologies  #
#  Copyright (C) 2015 Daniele Pantaleone <pantaleone@dis.uniroma1.it>    #
#                                                                        #
#  This program is free software: you can redistribute it and/or modify  #
#  it under the terms of the GNU General Public License as published by  #
#  the Free Software Foundation, either version 3 of the License, or     #
#  (at your option) any later version.                                   #
#                                                                        #
#  This program is distributed in the hope that it will be useful,       #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
#  GNU General Public License for more details.                          #
#                                                                        #
#  You should have received a copy of the GNU General Public License     #
#  along with this program. If not, see <http://www.gnu.org/licenses/>.  #
#                                                                        #
#  #####################                          #####################  #
#                                                                        #
#  Graphol is developed by members of the DASI-lab group of the          #
#  Dipartimento di Ingegneria Informatica, Automatica e Gestionale       #
#  A.Ruberti at Sapienza University of Rome: http://www.dis.uniroma1.it  #
#                                                                        #
#     - Domenico Lembo <lembo@dis.uniroma1.it>                           #
#     - Valerio Santarelli <santarelli@dis.uniroma1.it>                  #
#     - Domenico Fabio Savo <savo@dis.uniroma1.it>                       #
#     - Daniele Pantaleone <pantaleone@dis.uniroma1.it>                  #
#     - Marco Console <console@dis.uniroma1.it>                          #
#                                                                        #
##########################################################################


import sys

from enum import unique, Enum


@unique
class File(Enum):
    """
    This class defines supported filetypes.
    """
    __order__ = 'Csv Graphml Graphol Owl Pdf'

    Csv = 'Csv (*.csv)'
    Graphml = 'Graphml (*.graphml)'
    Graphol = 'Graphol (*.graphol)'
    Owl = 'Owl (*.owl)'
    Pdf = 'PDF (*.pdf)'

    @classmethod
    def forPath(cls, path):
        """
        Returns the File matching the given path.
        :type path: str
        :rtype: File
        """
        for x in cls:
            if path.endswith(x.extension):
                return x
        return None

    @classmethod
    def forValue(cls, value):
        """
        Returns the File matching the given value.
        :type value: str
        :rtype: File
        """
        for x in cls:
            if x.value == value:
                return x
        return None

    @property
    def extension(self):
        """
        The extension associated with the Enum member.
        :rtype: str
        """
        return {
            File.Csv: '.csv',
            File.Graphml: '.graphml',
            File.Graphol: '.graphol',
            File.Owl: '.owl',
            File.Pdf: '.pdf'
        }[self]


@unique
class Platform(Enum):
    """
    This class defines supported platforms.
    """
    __order__ = 'Darwin Linux Windows'

    Darwin = 'Darwin'
    Linux = 'Linux'
    Windows = 'Windows'
    Unknown = 'Unknown'

    @classmethod
    def identify(cls):
        """
        Returns the current platform identifier.
        :rtype: Platform
        """
        return Platform.forValue(sys.platform)

    @classmethod
    def forValue(cls, value):
        """
        Returns the platform identified by the the given value.
        :type value: str
        :rtype: Platform
        """
        if value.startswith('darwin'):
            return Platform.Darwin
        if value.startswith('linux'):
            return Platform.Linux
        if value.startswith('win') or value.startswith('cygwin'):
            return Platform.Windows
        return Platform.Unknown