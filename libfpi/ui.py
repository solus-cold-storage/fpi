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
    abar = None

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

        self.get_settings().set_property(
            "gtk-application-prefer-dark-theme", True)

        # Layout
        self.box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        self.add(self.box)

        self.abar = Gtk.ActionBar()
        self.box.pack_end(self.abar, False, False, 0)

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

        button = Gtk.Button("Install")
        lab_disclaimer = Gtk.Label(
            "This is a third party package and is not officially supported"
            " by Solus")
        img_warn = Gtk.Image.new_from_icon_name(
            "dialog-warning-symbolic", Gtk.IconSize.BUTTON)
        self.abar.pack_start(img_warn)
        self.abar.pack_start(lab_disclaimer)
        self.abar.pack_end(button)
        button.get_style_context().add_class("destructive-action")

        # Details
        dumb = Gtk.Label("Details ...")
        self._fix_label(dumb)
        dumb.set_property("margin", 12)
        self.stack.add_titled(dumb, "desc", "Details")

        # Files
        dumb = Gtk.Label("Files ...")
        self._fix_label(dumb)
        dumb.set_property("margin", 12)
        self.stack.add_titled(dumb, "files", "Files")

    def headerbar(self):
        header = Gtk.HeaderBar()
        header.set_show_close_button(True)

        self.stack_switcher = Gtk.StackSwitcher()
        header.set_custom_title(self.stack_switcher)
        self.stack_switcher.set_stack(self.stack)
        return header
