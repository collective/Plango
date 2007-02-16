# -*- coding: utf-8 -*-
#
# File: Install.py
#
# Plango - Copyright (c) 2006-2007 Paolo Melchiorre <paulox@paulox.net>
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Paolo Melchiorre <paulox@paulox.net>"""
__docformat__ = 'plaintext'


from StringIO import StringIO

from Products.Archetypes.Extensions.utils import install_subskin

from Products.Plango.config import PROJECTNAME
from Products.Plango.config import GLOBALS

def install(self, reinstall=False):
    """ External Method to install Plango """
    out = StringIO()
    print >> out, "Installation log of %s:" % PROJECTNAME
    install_subskin(self, out, GLOBALS)
    return out.getvalue()


def uninstall(self, reinstall=False):
    out = StringIO()
    print >> out, "Uninstallation log of %s:" % PROJECTNAME
    return out.getvalue()
