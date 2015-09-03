#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import subprocess
from sys import exit
from os import path
from os import listdir
from modis import Modis
from common import createPath
from dbServer import createConnection

class ClipImage:
    def __init__(self, program, product, archives_list, startDate, endDate,
            region, default_path):
        self.program = program
        self.product = product
        self.archives_list = archives_list
        self.startDate = startDate
        self.endDate = endDate
        self.region = region.upper()
        self.default_path = default_path
        self.mosaic_path = self.__makeMosaicPath(default_path)
        self.target_path = self.__makeTargetPath(default_path)
        self.shapefiles_path = self.__makeShapefilesPath()

        self.conn = createConnection()

    def __makeMosaicPath(self, tpath):
        return path.join(tpath, "mosaic")

    def __makeTargetPath(self, tpath):
        return path.join(tpath, "clip")

    def __makeShapefilesPath(self):
        aux = path.split(path.dirname(path.abspath(__file__)))

        return path.join(aux[0], "shapefiles")

    def __shapefileVerify(self, shapefile):
        if path.exists(self.shapefiles_path):
            list_shapefile = listdir(self.shapefiles_path)

            for shapf in list_shapefile:
                if shapf == shapefile + ".shp":
                    return True

            return False
        else:
            return False

    def __finishClip(self):
        print "finish here"



    def run(self):
        if self.program and self.product and self.archives_list \
            and self.startDate and self.endDate and self.target_path \
            and self.mosaic_path and self.shapefiles_path:
            createPath(self.target_path)

            if not path.exists(self.mosaic_path):
                exit("[CLIP MODULE     ] |-> Error: Directory %s does "
                    % self.mosaic_path + "not exist")

            if not path.exists(self.shapefiles_path):
                exit("[CLIP MODULE     ] |-> Error: Directory %s does "
                    % self.shapefiles_path + "not exist")

            if self.program.upper() == "MODIS":
                product = Modis(self.product)

            if product.exist:
                if path.exists(self.shapefiles_path):
                    if self.__shapefileVerify(self.region):
                        for archive in self.archives_list:
                            out_file = self.program + "_" + self.product \
                                    + "_" + self.startDate + "_" \
                                    + self.endDate + "_" + archive[0] + "_" \
                                    + self.region + ".tif"

                            shapefile = self.region + ".shp"

                            in_path = path.join(self.mosaic_path, archive[1])
                            out_path = path.join(self.target_path, out_file)
                            shape_path = path.join(self.shapefiles_path,
                                    shapefile)

                            args = ["gdalwarp", "-cutline", shape_path, in_path,
                                    out_path]

                            subprocess.call(args)

                        self.__finishClip()

                        return True
                    else:
                        print("[CLIP MODULE     ] |-> Error: %s shapefile does"
                                % (self.region + ".shp") + " not exist")

                        print "here1"
                        return False
                else:
                    print("[CLIP MODULE     ] |-> Error: %s path does not exist"
                            % self.shapefiles_path)

                    print "here2"
                    return False
            else:
                print("[CLIP MODULE     ] |-> Error: %s product does not "
                    % self.product + "supported")

                print "here3"
                return False
