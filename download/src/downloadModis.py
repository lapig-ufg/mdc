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
import os
from sys import exit
from os import path
from os import makedirs
from pymodis import downmodis
from region import Region
from dateModis import DateModis

class DownloadModis:
    """ A class to download the specific product, region and date modis data """

    def __init__(self, product, region, start, end,
            target_path = "/home/" + getpass.getuser() +"/Maps"):
        """ Initialize function """

        self.product = product
        self.start = start
        self.end = end
        self.target_path = target_path
        # return an object which have all tiles of the region
        self.region = Region(region)

    def run(self):
        """ Method which run download of modis data """

        """ verify if the directory exist if not try to create """
        if not path.exists(self.target_path):
            try:
                makedirs(self.target_path)
            except:
                exit("-> Error: Directory %s does " % self.target_path \
                        + "not exist and it is impossible to create")

        # all parameters exist
        if self.product and self.start and self.end and self.target_path \
                and self.region:
            # make a partitions list of dates
            dates = DateModis(self.product, self.start, self.end)

            # download the specific data for all date in the list
            for date in dates.datesList:
                print "-> Preparing to download data between " + date["start"] \
                        + " and " + date["end"] + "..."

                # create a download modis object
                modisObj = downmodis.downModis(url="http://e4ftl01.cr.usgs.gov",
                    user="anonymous", password=None, path="MOLT", delta=10,
                    timeout=30, destinationFolder=self.target_path, jpg=False,
                    debug=False, tiles=self.region.printIds(),
                    today=date["start"], enddate=date["end"],
                    product=self.product)

                # try to make the download
                try:
                    modisObj.connect()
                    if modisObj.nconnection <= 20:
                        print " |-> Start download..."
                        modisObj.downloadsAllDay(clean=True, allDays=False)
                        print " |-> Download finished..."
                    else:
                        print " |-> Error: Problem with the connection!"
                except:
                    print " |-> Error: Problem with download..."

            return True
        # problem with one or more parameters
        else:
            return False
