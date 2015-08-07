#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import getpass
from sys import exit
from os import path
from os import makedirs
from region import Region

class DownloadLandsat:
    def __init__(self, product, name, start, end,
            target = "/home/" + getpass.getuser() +"/Maps"):
        self.product = product
        self.start = start
        self.end = end
        self.target = target
        self.region = Region(name)

    def run():
        print "Not implemented yet"
