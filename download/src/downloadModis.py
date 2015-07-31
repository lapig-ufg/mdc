#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
# (c) Copyright Marcelo Perini Veloso 2015
# ------------------------------------------
import getpass
from sys import exit
from os import path
from os import makedirs
from pymodis import downmodis
from region import Region
from dateModis import DateModis

class DownloadModis:
    def __init__(self, product, name, start, end,
            target = "/home/" + getpass.getuser() +"/Maps"):
        self.product = product
        self.start = start
        self.end = end
        self.target = target
        self.region = Region(name)

    def run(self):
        if not path.exists(self.target):
            try:
                os.makedirs(self.target)
            except:
                exit("-> Error: Directory %s does not exist " % self.target \
                        + "and it is impossible to create")

        if self.product and self.start and self.end and self.target \
                and self.region:
            dates = DateModis(self.product, self.start, self.end)

            for date in dates.datesList:
                print "-> Preparing download data between " + date["start"] \
                        + " and " + date["end"] + "..."

                modisObj = downmodis.downModis(url="http://e4ftl01.cr.usgs.gov",
                    user="anonymous", password=None, path="MOLT", delta=10,
                    timeout=30, destinationFolder=self.target, jpg=False,
                    debug=False, tiles=self.region.printIds(),
                    today=date["start"], enddate=date["end"],
                    product=self.product)

                modisObj.connect()
                if modisObj.nconnection <= 20:
                    print " |-> Start download..."
                    modisObj.downloadsAllDay(clean=True, allDays=False)
                    print " |-> Download finished..."
                else:
                    exit(" |-> Error: Problem with the connection!")

            return True
        else:
            return False
