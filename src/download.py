#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
from sys import argv
from downloadModis import DownloadModis
from downloadLandsat import DownloadLandsat
from common import mapDict
from common import createDefaultPath

def download(program, product, region, startDate, endDate,
        targetPath = createDefaultPath()):
    if program and product and region and startDate and endDate:
        if program.upper() == "MODIS":
            imgDownload = DownloadModis(product=product,
                    region=region, start=startDate,
                    end=endDate)
        elif program.upper() == "LANDSAT":
            imgDownload = DownloadLandsat(product=product,
                    region=region, start=startDate,
                    end=endDate)
        else:
            return False

        if targetPath:
            imgDownload.target = targetPath

        if imgDownload.run() == True:
            print "--> Finish download module"
        else:
            print "--> Was not possible to make the download"

        return True

usage = """\
Usage: %s [OPTIONS]
    -d      name of satellite observation program
    -p      product name
    -r      download specifics tiles of this region
    -s      start date of image that will be download
    -e      end date of images that will be download
    [-t]    path to directory where the files will be stored
""" % argv[0]

"""
def main():
    args_dict = mapDict(usage)

    if "-d" not in args_dict or "-p" not in args_dict or "-s" not in args_dict \
            or "-e" not in args_dict or "-r" not in args_dict:
        exit(usage)
    else:
        if args_dict["-d"].upper() == "MODIS":
            imgDownload = DownloadModis(product=args_dict["-p"],
                    region=args_dict["-r"], start=args_dict["-s"],
                    end=args_dict["-e"])
        elif args_dict["-d"].upper() == "LANDSAT":
            imgDownload = DownloadLandsat(product=args_dict["-p"],
                    name=args_dict["-r"], start=args_dict["-s"],
                    end=args_dict["-e"])
        else:
            printUsage()

        if "-t" in args_dict:
            imgDownload.target = args_dict["-t"]

        if imgDownload.run() == True:
            print "--> Finish download module"
        else:
            print "--> Was not possible to make the download"

if __name__ == "__main__":
    main()
"""
