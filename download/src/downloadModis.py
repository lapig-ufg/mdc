#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import os
import redis
import shutil
import json
from sys import exit
from os import path
from os import makedirs
from pymodis import downmodis
from region import Region
from dateModis import DateModis

# make the work default path
home_path = os.path.expanduser("~")
default_path = os.path.join(home_path, "Maps")

class DownloadModis:
    """ A class to download the specific product, region and date modis data """

    def __init__(self, product, region, start, end, target_path = default_path):
        """ Initialize function """

        self.product = product
        self.start = start
        self.end = end
        self.target_path = target_path
        # return an object which have all tiles of the region
        self.region = Region(region)

        self.conn = redis.StrictRedis(host="localhost", port=6379, db=0)

        try:
            self.conn.set("download", '{ "archives" : [] }')
        except :
            exit("-> Error: Connection refused to localhost:6379")

    def __finishDownload(self, path_one, path_two):
        listArchives = os.listdir(path_one)

        try:
            jsonTxt = self.conn.get("download")
        except:
            exit(" |-> Error: Connection refused to localhost:6379")

        if jsonTxt != None:
            try:
                jsonObj = json.loads(jsonTxt)
            except ValueError as msg:
                exit(" |-> Error: Corrupt value message in Redis: %s" % msg)

            if path.exists(path_one) and path.exists(path_two):
                for archive in listArchives:
                    try:
                        shutil.move(os.path.join(path_one, archive), path_two)

                        jsonObj["archives"].append(archive)
                    except IOError as msg:
                        print(" |-> Error: %s" % msg)
                    except KeyError as msg:
                        exit(" |-> Error: Corrupt value message in Redis: %s" %
                                msg)

                try:
                    jsonTxt = json.dumps(jsonObj)
                except TypeError as msg:
                    exit(" |-> Error: Corrupt value message in Redis: %s" % msg)

                try:
                    self.conn.set("download", jsonTxt)
                except :
                    exit("-> Error: Connection refused to localhost:6379")

                return True
            else:
                return False
        else:
            exit(" |-> Error: Corrupt value message in Redis")


    def run(self):
        """ Method which run download of modis data """

        print self.target_path
        """ verify if the directory exist if not try to create """
        if not path.exists(self.target_path):
            try:
                makedirs(self.target_path)
            except:
                exit("-> Error: Directory %s does " % self.target_path \
                        + "not exist and it is impossible to create")


        downloading_path = os.path.join(self.target_path, "downloading")
        downloaded_path = os.path.join(self.target_path, "downloaded")

        print downloading_path
        if not path.exists(downloading_path):
            try:
                makedirs(downloading_path)
            except:
                exit("-> Error: Directory %s does " % downloading_path \
                        + "not exist and it is impossible to create")

        print downloaded_path
        if not path.exists(downloaded_path):
            try:
                makedirs(downloaded_path)
            except:
                exit("-> Error: Directory %s does " % downloaded_path \
                        + "not exist and it is impossible to create")

        # all parameters exist
        if self.product and self.start and self.end and self.target_path \
                and self.region:
            # make a partitions list of dates
            dates = DateModis(self.product, self.start, self.end)

            # download the specific data for all date in the list
            for date in dates.datesList:
                dict_path = self.product + "_" + date["start"] + "_" + date["end"]

                down_path = os.path.join(downloading_path, dict_path)

                if not path.exists(down_path):
                    try:
                        makedirs(down_path)
                    except:
                        print("-> Error: Directory %s does " % down_path \
                            + "not exist and it is impossible to create. " \
                            + "The download %s product " % self.product \
                            + "relative of %s and " % date["start"] \
                            + "%s will not be done" % date["end"])
                        break

                print "-> Preparing to download data between " + date["start"] \
                        + " and " + date["end"] + "..."

                # create a download modis object
                modisObj = downmodis.downModis(url="http://e4ftl01.cr.usgs.gov",
                    user="anonymous", password=None, path="MOLT", delta=10,
                    timeout=30, destinationFolder=down_path, jpg=False,
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

                        self.__finishDownload(down_path, downloaded_path)
                    else:
                        print " |-> Error: Problem with the connection!"
                except:
                    print " |-> Error: Problem with download..."

            return True
        # problem with one or more parameters
        else:
            return False
