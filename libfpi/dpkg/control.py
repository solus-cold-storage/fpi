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


class Control:

    field_set = None
    current_field = None
    mandatory_fields = [
        "package",
        "version",
        "description"
    ]

    def __init__(self):
        self.field_set = dict()

    def parse(self, cfile):
        """ Begin parsing the file - raise errors if go boom """
        with open(cfile, "r") as inp:
            for line in inp.readlines():
                line = line.replace("\r", "").replace("\n", "").rstrip()
                self.push_line(line)
        for field in self.mandatory_fields:
            if field not in self.field_set:
                raise RuntimeError("Missing field {}".format(field))

    def push_line(self, line):
        """ Push a line from the control file for parsing """
        splits = line.split(":")
        key = splits[0].lower()
        # Debian control run on
        if line.startswith(" "):
            self.merge_with(self.current_field, line.lstrip())
            return
        value = ":".join(splits[1:])
        self.push_value(key, value)

    def push_value(self, key, value):
        """ Push a simple key = value """
        self.field_set[key] = value.strip()
        self.current_field = key

    def merge_with(self, field, value):
        """ Merge a value with an existing field through control run-on """
        if field is None:
            raise RuntimeError("Tried to merge run-on with missing field")
        if field not in self.field_set:
            raise RuntimeError("Merging with missing field {}".format(field))
        self.field_set[field] += "\n" + value.strip()

    def get_name(self):
        """ Return the public sane name of the package """
        return self.field_set["package"]

    def get_summary(self):
        """ Return the public sane summary of the package """
        return self.field_set["description"].split("\n")[0]

    def get_description(self):
        """ Return the public sane description of the package """
        lines = self.field_set["description"].split("\n")
        if len(lines) < 2:
            return lines[0]
        return "\n".join(lines[1:])
