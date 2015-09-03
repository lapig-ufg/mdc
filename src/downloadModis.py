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
import shutil
import json
import datetime
from sys import exit
from os import path
from os import makedirs
from dbServer import createConnection
from pymodis import downmodis
from region import Region
from modis import Modis

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

        # make a connection with redis server
        self.conn = createConnection()

    def __isHdf(self, name):
        return name.split('.')[-1] == "hdf"

    def __isXml(self, name):
        return name.split('.')[-1] == "xml"

    def __finishDownload(self, path_one, path_two, initDate, endDate):
        """Function which move all finished archives to downloaded directory"""

        # get a list of all archives in path_one directory
        listArchives = os.listdir(path_one)

        # if one of this paths not exist exit
        if path.exists(path_one) and path.exists(path_two):
            archDict = { "archives" : [], "product" : self.product }

            # move HDFs archives in path_one to path_two
            for archive in listArchives:
                if self.__isHdf(archive) or self.__isXml(archive):
                    try:
                        shutil.move(os.path.join(path_one, archive),
                                os.path.join(path_two, archive))

                        if self.__isHdf(archive):
                            archDict["archives"].append(archive)

                    except IOError as msg:
                        print("[DOWNLOAD MODULE ] |-> Error: Was not possible " \
                                + "to move %s" % msg)

            baseKey = "DOWNLOAD_MODIS_" + self.product.upper() + "_" \
                    + initDate + "_" + endDate

            jsonTxt = json.dumps(archDict)

            try:
                self.conn.set(baseKey, jsonTxt)
            except:
                print("[DOWNLOAD MODULE ] |-> Error: Problem with redis " \
                        + "database connection...")

            print "[DOWNLOAD MODULE ] |-> Download finished..."

    def __makeDateList(self, tmpColect, initProgram = None, endProgram = None):
        """ create a list of dates """
        startDate = self.__convertDate(self.start)
        endDate = self.__convertDate(self.end)

        if initProgram != None and startDate < initProgram:
            startDate = initProgram

        if endProgram != None and endDate > endProgram:
            endDate = endProgram

        dateList = []

        start = startDate
        end = start

        # while the end date used to next date pair are less than endDate
        while end < endDate:
            # add the start date to colect day
            end = start + datetime.timedelta(days=tmpColect)

            # if the end date of next date pair is more than endDate use endDate
            if end > endDate:
                end = endDate

            # append an dict of start date and end date pair
            dateList.append({"start" : start.strftime("%Y-%m-%d"),
                "end" : end.strftime("%Y-%m-%d")})

            # add 1 day to end date and put into start date
            # start = end + datetime.timedelta(days=1)
            start = end

        return dateList

    def __convertDate(self, strDate):
        try:
            return datetime.datetime.strptime(strDate, "%Y-%m-%d")
        except:
            exit("[DOWNLOAD MODULE ] |-> Error: '%s' have a " % strDate \
                    + "wrong date format, use YYYY-MM-DD")

    def run(self):
        """ Method which run download of modis data """

        """ verify if the directory exist if not try to create """
        if not path.exists(self.target_path):
            try:
                makedirs(self.target_path)
            except:
                exit("[DOWNLOAD MODULE ] |-> Error: Directory " \
                        + "%s does " % self.target_path + "not exist and it " \
                        + "is impossible to create")


        downloading_path = os.path.join(self.target_path, "downloading")
        downloaded_path = os.path.join(self.target_path, "downloaded")

        if not path.exists(downloading_path):
            try:
                makedirs(downloading_path)
            except:
                exit("[DOWNLOAD MODULE ] |-> Error: Directory " \
                        + "%s does " % downloading_path + "not exist and it " \
                        + "is impossible to create")

        if not path.exists(downloaded_path):
            try:
                makedirs(downloaded_path)
            except:
                exit("[DOWNLOAD MODULE ] |-> Error: Directory " \
                        + "%s does " % downloaded_path + "not exist and it " \
                        + "is impossible to create")

        # all parameters exist
        if self.product and self.start and self.end and self.target_path \
                and self.region:

            modis = Modis(self.product)

            # if the product exist
            if modis.temporalColect != None:
                # make a partitions list of dates
                dates = self.__makeDateList(modis.temporalColect)

                # download the specific data for all date in the list
                for date in dates:
                    dict_path = self.product + "_" + date["start"] + "_" \
                            + date["end"]

                    down_path = os.path.join(downloading_path, dict_path)

                    if not path.exists(down_path):
                        try:
                            makedirs(down_path)
                        except:
                            print("[DOWNLOAD MODULE ] |-> Error: Directory " \
                                    + "%s does " % down_path + "not exist " \
                                    + "and it is impossible to create. The " \
                                    + "download %s product " % self.product \
                                    + "relative of %s and " % date["start"] \
                                    + "%s will not be done" % date["end"])
                            break

                    print "[DOWNLOAD MODULE ] |-> Preparing download " \
                            + "data between " + date["start"] + " and " + date["end"] + "..."

                    if modis.no_tiles:
                        # create a download modis object
                        modisObj = downmodis.downModis(
                                url="http://e4ftl01.cr.usgs.gov",
                                user="anonymous", password=None, path="MOLT",
                                delta=10, timeout=30,
                                destinationFolder=down_path, jpg=False,
                                debug=False, today=date["start"],
                                enddate=date["end"], product=self.product)
                    else:
                        # create a download modis object
                        modisObj = downmodis.downModis(
                                url="http://e4ftl01.cr.usgs.gov",
                                user="anonymous", password=None, path="MOLT",
                                delta=10, timeout=30,
                                destinationFolder=down_path, jpg=False,
                                debug=False, tiles=self.region.printIds(),
                                today=date["start"], enddate=date["end"],
                                product=self.product)

                    # try to make the download
                    try:
                        modisObj.connect()

                        if modisObj.nconnection <= 20:
                            print "[DOWNLOAD MODULE ] |-> Start download..."
                            modisObj.downloadsAllDay(clean=True, allDays=False)
                            self.__finishDownload(down_path, downloaded_path,
                                    date["start"], date["end"])
                        else:
                            print "[DOWNLOAD MODULE ] |-> Error: Problem with " \
                                    + "the connection!"
                    except:
                        print "[DOWNLOAD MODULE ] |-> Error: Problem with " \
                                + "download..."

                    if path.exists(down_path):
                        try:
                            shutil.rmtree(down_path)
                        except OSError:
                            print("[DOWNLOAD MODULE ] |-> Error: Impossible " \
                                    + "to remove %s", path_one)

                return True
            else:
                return False
        # problem with one or more parameters
        else:
            return False
