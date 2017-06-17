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

    box = None
    stack = None
    stack_switcher = None

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

        # Layout
        self.box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        self.box.set_border_width(12)
        self.add(self.box)
        self.build_contents()

        # Finalize the window itself
        self.set_titlebar(self.headerbar())
        self.set_title("Foreign Package Installer")
        self.set_icon_name("system-software-install")
        self.set_size_request(600, 450)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.show_all()

    def _fix_label(self, label):
        label.set_halign(Gtk.Align.START)
        label.set_valign(Gtk.Align.START)

    def build_contents(self):
        """ Build the main UI display regions """
        self.stack = Gtk.Stack()
        self.box.pack_start(self.stack, True, True, 0)

        # Details
        dumb = Gtk.Label("Details ...")
        self._fix_label(dumb)
        self.stack.add_titled(dumb, "desc", "Details")

        # Files
        dumb = Gtk.Label("Files ...")
        self._fix_label(dumb)
        self.stack.add_titled(dumb, "files", "Files")

    def headerbar(self):
        header = Gtk.HeaderBar()
        header.set_show_close_button(True)

        self.stack_switcher = Gtk.StackSwitcher()
        header.set_custom_title(self.stack_switcher)
        self.stack_switcher.set_stack(self.stack)

        button_action = Gtk.Button("Install")
        button_action.get_style_context().add_class("suggested-action")
        header.pack_start(button_action)
        return header
