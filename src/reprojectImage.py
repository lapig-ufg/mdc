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
from common import createPath
from dbServer import createConnection

class reprojectImage:
    """ Class which receive a list of hdf archives and convert to tif
      " format
      """

    def __init__(self, product, archive_list, start_date, end_date,
            default_path, mrt_path):
        """ Constructor method """

        self.product = product
        self.archive_list = archive_list
        self.startDate = start_date
        self.endDate = end_date

        self.default_path = default_path
        self.target_path = path.join(self.default_path, "reproject")
        self.reprojecting_path = path.join(self.target_path, "reprojecting")
        self.download_path = path.join(self.default_path, "download")

        self.mrt_path = mrt_path

        # make a connection with redis server
        self.conn = createConnection()

    def __createTifName(self, archive):
        """ This method receive a string name and replace the hdf
          "  extencion to tif
          """

        return archive.replace("hdf", "tif")

    def __isTif(self, archive):
        """ This method verify if archive have a tif extensin """

        return archive.split('.')[-1] == "tif"

    def __getBand(self, archive):
        return archive.split('.')[-2]

    def __finishConvert(self):
        """ This method read all archives in converted_path add than in
          " a dictionary, convert into a json text and push to redis
          " database
          """

        if path.exists(self.reprojecting_path):
            # read all files in converting_path
            listArchives = listdir(self.reprojecting_path)

            archDict = { "bands" : { } }

            """ move all archives in converting path to converted path
              " and apend into archDict
              """
            for archive in listArchives:
                # if the archive is tif format
                if self.__isTif(archive):
                    try:
                        shutil.move(path.join(self.reprojecting_path, archive),
                                path.join(self.target_path, archive))

                        band = self.__getBand(archive)

                        try:
                            archDict["bands"][band].append(archive)
                        except KeyError:
                            archDict["bands"][band] = []
                            archDict["bands"][band].append(archive)

                    except IOError as msg:
                        print("[REPROJECT MODULE] |-> Error: Was not " \
                                + "possible to move %s" % msg)

            baseKey = "REPROJECT_MODIS_" + self.product.upper() + "_" \
                    + self.startDate + "_" + self.endDate

            jsonTxt = json.dumps(archDict)

            try:
                self.conn.set(baseKey, jsonTxt)
            except:
                print("[REPROJECT MODULE] |-> Error: Problem with redis " \
                        + "database connection...")
        else:
            exit("[REPROJECT MODULE] |-> Error: Directory %s does "
                    % self.reprojecting_path + "not exist")

    def run(self):
        """ This method read the hdf files in archive_list and convert
          " to tif format
          """

        print("[REPROJECT MODULE]--> Start the reprojection...")

        if not createPath(self.reprojecting_path):
            exit("[REPROJECT MODULE ] |-> Error: Directory %s does not exist "
                    % self.reprojecting_path + "and it is impossible to create")

        if not path.exists(self.download_path):
            exit("[REPROJECT MODULE] |-> Error: Directory %s does "
                    % self.download_path + "not exist.")

        if self.archive_list != None:
            modis = Modis(self.product)

            if modis.exist:
                # create the spectral to convert the image of all band
                baseLayer = []
                for i in range(len(modis.layers)):
                    baseLayer.append('0')

                baseStr = []
                for i in range(len(modis.layers)):
                    aux = list(baseLayer)
                    aux[i] = '1'
                    txt = "( "

                    for letter in aux:
                        txt += letter + ' '

                    txt += ')'
                    baseStr.append(txt)

                for archive in self.archive_list:
                    archive_path = path.join(self.download_path, archive)

                    if path.exists(archive_path):
                        for base in baseStr:

                            output_path = path.join(self.reprojecting_path,
                                    self.__createTifName(archive))

                            modisParse = parsemodis.parseModis(archive_path)
                            confname = modisParse.confResample(spectral=base,
                                    output=output_path)

                            modisCover = convertmodis.convertModis(
                                    hdfname=archive_path, confile=confname,
                                    mrtpath=self.mrt_path)

                            modisCover.run()
                    else:
                        print("[REPROJECT MODULE] |-> Error: %s does not exist"
                            % archive_path)
                        exit(1)

                self.__finishConvert()

                return True
            else:
                print("[REPROJECT MODULE] |-> Error: %s product does not " \
                        + "supported" % self.product)
                exit(1)
        else:
            print "[REPROJECT MODULE] |-> Error: The archive list are empty"
            exit(1)
