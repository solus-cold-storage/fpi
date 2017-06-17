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


class Package:

    metaset = None

    def __init__(self):
        self.metaset = dict()

    def version(self):
        """ Return the packages version """
        return self.get_meta("version")

    def name(self):
        """ Return the name of the package """
        return self.get_meta("name")

    def summary(self):
        """ Return the summary of the package """
        return self.get_meta("summary")

    def description(self):
        """ Return the description of the package """
        return self.get_meta("description")

    def release(self):
        """ Return the release for the package """
        return self.get_meta("release")

    def get_meta(self, key):
        """ Return a value for the given key """
        if key not in self.metaset:
            raise RuntimeError("Unsupported meta key '{}'".format(key))
        return self.metaset[key]
