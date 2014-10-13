#-*- coding: utf-8 -*-

"""
 (c) 2014 - Copyright Johan Cwiklinski <johan@x-tnd.be>

 Distributed under License GPLv3 or later
 You can find a copy of this license on the website
 http://www.gnu.org/licenses/gpl.html

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 MA 02110-1301, USA.
"""


class FedocalBabel(object):
    """Wrapper for Babel class, if flask-babel is missing"""

    def __init__(self):
        pass

    def localeselector(self, f):
        return f


def get_babel(app):
    try:
        from flask.ext.babel import Babel
        return Babel(app)
    except:
        return FedocalBabel()


def gettext(string, **variables):
    """Wrapper for gettext functions, if flask-babel is missing"""
    try:
        from flask.ext.babel import gettext
        return gettext(string, variables)
    except:
        return string


def lazy_gettext(string, **variables):
    """Wrapper for lazy_gettext function, if flask-babel is missing"""
    try:
        from flask.ext.babel import lazy_gettext
        return lazy_gettext(string, variables)
    except:
        return string


def format_datetime(datetime=None, format=None, rebase=True):
    """Wrapper for lazy_gettext function, if flask-babel is missing"""
    try:
        from flask.ext.babel import format_datetime
        return format_datetime(datetime, format, rebase)
    except:
        return datetime


def get_locale():
    try:
        from flask.ext.babel import get_locale
        return get_locale()
    except:
        return 'en'
