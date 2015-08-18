#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import shutil
import json
from sys import exit
from os import path
from os import makedirs
from os import listdir
from pymodis import parsemodis
from pymodis import convertmodis
from modis import Modis
from dbServer import createConnection

def createDefaultPath():
    # default work directory
    home_path = path.expanduser("~")
    default_path = path.join(home_path, "Maps")
    return default_path

def createMrtPath():
    home_path = path.expanduser("~")
    mrt_path = path.join(home_path, ".mrt")
    return mrt_path

class convert:
    def __init__(self, product, archive_list, start_date, end_date,
            default_path = createDefaultPath(), mrt_path = createMrtPath()):
        self.product = product
        self.archive_list = archive_list
        self.startDate = start_date
        self.endDate = end_date
        self.downloaded_path = self.__makeDownloadedPath(default_path)
        self.target_path = self.__makeTargetPath(default_path)
        self.mrt_path = mrt_path

        self.conn = createConnection()


    def __makeDownloadedPath(self, tpath):
        return path.join(tpath, "downloaded")

    def __makeTargetPath(self, tpath):
        return path.join(tpath, "converted")

    def __createTifName(self, archive):
        return archive.replace("hdf", "tif")

    def __createPath(self, tpath):
        if not path.exists(tpath):
            try:
                makedirs(tpath)
            except:
                exit(" |-> Error: Directory %s does " % tpath \
                        + "not exist and it is impossible to create")

    def __isTif(self, archive):
        return archive.split('.')[-1] == "tif"

    def __finishConvert(self, converting_path):
        if path.exists(converting_path):
            listArchives = listdir(converting_path)

            archDict = { "archives" : [] }

            for archive in listArchives:
                if self.__isTif(archive):
                    try:
                        shutil.move(path.join(converting_path, archive),
                                path.join(self.target_path, archive))

                        archDict["archives"].append(archive)

                    except IOError as msg:
                        print(" |-> Error: Was not possible to move %s" % msg)

            baseKey = "REPROJECT_MODIS_" + self.product.upper() + "_" \
                    + self.startDate + "_" + self.endDate

            jsonTxt = json.dumps(archDict)

            try:
                self.conn.set(baseKey, jsonTxt)
            except:
                print(" |-> Error: Problem with redis database connection...")


            print(" |-> Finish convert process...")
        else:
            exit(" |-> Error: Directory %s does " % converting_path \
                    + "not exist")

    def run(self):
        print("--> Start the reprojection...")

        self.__createPath(self.target_path)

        if not path.exists(self.downloaded_path):
            exit(" |-> Error: Directory %s does " % downloaded_path \
                    + "not exist.")

        if self.archive_list != None:
            modis = Modis(self.product)

            baseLayer = []
            for i in range(modis.nBand):
                baseLayer.append('0')

            baseStr = []
            for i in range(modis.nBand):
                aux = list(baseLayer)
                aux[i] = '1'
                txt = "( "

                for letter in aux:
                    txt += letter + ' '

                txt += ')'
                baseStr.append(txt)

            if modis.exist:
                converting_path = path.join(self.target_path, "converting")

                self.__createPath(converting_path)

                for archive in self.archive_list:
                    archive_path = path.join(self.downloaded_path, archive)
                    #cont_band = 1

                    if path.exists(archive_path):
                        for base in baseStr:

                            #output_path = path.join(self.target_path,
                            #        self.__createTifName(str(cont_band) \
                            #                + "_" + archive))

                            output_path = path.join(converting_path,
                                    self.__createTifName(archive))

                            modisParse = parsemodis.parseModis(archive_path)
                            confname = modisParse.confResample(spectral=base,
                                    output=output_path)

                            modisCover = convertmodis.convertModis(
                                    hdfname=archive_path, confile=confname,
                                    mrtpath=self.mrt_path)

                            #cont_band += 1

                            modisCover.run()
                    else:
                        exit(" |-> Error: %s does not exist" % archive_path)

                self.__finishConvert(converting_path)
            else:
                exit(" |-> Error: %s product does not supported" % self.product)
        else:
            exit(" |-> Error: The archive list are empty")
