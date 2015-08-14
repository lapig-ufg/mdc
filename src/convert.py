#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
from sys import exit
from os import path
from os import makedirs
from pymodis import parsemodis
from pymodis import convertmodis
from modis import Modis

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
    def __init__(self, product, archive_list,
            default_path = createDefaultPath(), mrt_path = createMrtPath()):
        self.product = product
        self.archive_list = archive_list
        self.downloaded_path = self.__makeDownloadedPath(default_path)
        self.target_path = self.__makeTargetPath(default_path)
        self.mrt_path = mrt_path

    def __makeDownloadedPath(self, tpath):
        return path.join(tpath, "downloaded")

    def __makeTargetPath(self, tpath):
        return path.join(tpath, "converted")

    def __createTifName(self, archive):
        return archive.replace("hdf", "tif")

    def __finishConvert(self):
        print "Here"

    def run(self):
        print("--> Start the reprojection...")

        if not path.exists(self.target_path):
            try:
                makedirs(self.target_path)
            except:
                exit(" |-> Error: Directory %s does " % self.target_path \
                        + "not exist and it is impossible to create")

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
                for archive in self.archive_list:
                    archive_path = path.join(self.downloaded_path, archive)
                    #cont_band = 1

                    if path.exists(archive_path):
                        for base in baseStr:

                            #output_path = path.join(self.target_path,
                            #        self.__createTifName(str(cont_band) \
                            #                + "_" + archive))

                            output_path = path.join(self.target_path,
                                    self.__createTifName(archive))

                            modisParse = parsemodis.parseModis(archive_path)
                            confname = modisParse.confResample(spectral = base,
                                    output = output_path)

                            modisCover = convertmodis.convertModis(
                                    hdfname=archive_path, confile=confname,
                                    mrtpath=self.mrt_path)

                            #cont_band += 1

                            modisCover.run()
                    else:
                        exit(" |-> Error: %s does not exist" % archive_path)
            else:
                exit(" |-> Error: %s product does not supported" % self.product)
        else:
            exit(" |-> Error: The archive list are empty")

        print(" |-> Finish convert process...")
