# -*- coding: utf-8 -*-
#
# File: __init__.py
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

# Register our skins directory - this makes it available via portal_skins.

from Products.CMFCore import DirectoryView

from Products.Plango.config import GLOBALS

DirectoryView.registerDirectory('skins', GLOBALS)