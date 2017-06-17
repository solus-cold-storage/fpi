#!/bin/true
# -*- coding: utf-8 -*-
#
#  This file is part of fpi
#
#  Copyright 2017 Ikey Doherty <ikey@solus-project.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#


from gi.repository import Gtk


class FpiWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)
        self.show_all()
