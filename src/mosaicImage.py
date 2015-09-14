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
import json
from sys import exit
from os import path
from os import remove
from common import createPath
from common import ifExistRemoveFile
from modis import Modis
from dbServer import createConnection

class MosaicImage:
    def __init__(self, program, product, region, bands_archive_list, startDate, endDate,
            formula, default_path):
        self.program = program
        self.product = product
        self.region = region
        self.archive_list = bands_archive_list
        self.startDate = startDate
        self.endDate = endDate
        self.formula = formula

        self.default_path = default_path
        self.reproject_path = path.join(self.default_path, "reproject")
        self.target_path = path.join(self.default_path, "mosaic")

        # make a connection with redis server
        self.conn = createConnection()

    def __finishMosaic(self, out_files):
        baseKey = "MOSAIC_" + self.program.upper() + "_" \
                + self.product.upper() + "_" + self.startDate \
                + "_" + self.endDate

        archDict = { "archives" : out_files, "program" : self.program,
                "product" : self.product, "region": self.region,
                "startDate" : self.startDate, "endDate" : self.endDate,
                "formula" : self.formula, "defaultPath" : self.default_path }

        jsonTxt = json.dumps(archDict)

        try:
            self.conn.set(baseKey, jsonTxt)
        except:
            print("[MOSAIC MODULE   ] |-> Error: Problem with redis database " \
                    + "connection...")

    def run(self):
        if self.program and self.product and self.archive_list \
                and self.startDate and self.endDate and self.target_path \
                and self.reproject_path:

            if not createPath(self.target_path):
                exit("[MOSAIC MODULE   ] |-> Error: Directory %s does "
                        % self.target_path + "not exist.")


            if not path.exists(self.reproject_path):
                exit("[MOSAIC MODULE   ] |-> Error: Directory %s does "
                        % self.reproject_path + "not exist.")

            if self.program.upper() == "MODIS":
                product = Modis(self.product)

            if product.exist:
                out_files = []

                for band in self.bands_archive_list:
                    filenames = []

                    file = self.program + "_" + self.product + "_" \
                            + self.startDate + "_" + self.endDate + "_" \
                            + band + ".tif"

                    out_file = path.join(self.target_path, file)

                    for archive in self.archive_list[band]:
                        filename = path.join(self.reproject_path, archive)

                        if path.exists(filename):
                            filenames.append(filename)

                    if band in product.layers:
                        ifExistRemoveFile(out_file)

                        args = ["gdal_merge.py"]

                        # encontrar uma forma de utilizar uma range
                        # de fill
                        if product.layers[band] is not None:
                            args += ["-n", product.layers[band], "-a_nodata",
                                    product.layers[band]]

                        args += ["-o", out_file]

                        args += ["-co", "COMPRESS=LZW",
                                "-co", "INTERLEAVE=BAND",
                                "-co", "TILED=YES",
                                "-co","BIGTIFF=IF_NEEDED"]

                        args += filenames

                        print("[MOSAIC MODULE   ]  |-> Start mosaic of %s"
                                % band)
                        subprocess.call(args, stdout=subprocess.PIPE)
                        print("[MOSAIC MODULE   ]   |-> End mosaic of %s"
                                % band)

                        out_files.append([band, file])

                if len(out_files) > 0:
                    self.__finishMosaic(out_files)
            else:
                print "[MOSAIC MODULE   ] |-> Error: %s product does not " \
                        + "supported" % self.product
                return False
        else:
            return False

        return True
