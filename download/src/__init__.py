#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Init script to download module
#
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
# (c) Copyright Marcelo Perini Veloso 2015
# ------------------------------------------
import sys
from downloadModis import DownloadModis
from downloadLandsat import DownloadLandsat

def print_usage(argv):
    #Print usage and exit
    sys.exit("Usage: %s -d {Program Specification} -p {Product} -r {Region} " %
            argv[0] \
                    + "-s {Start Date} -e {End Date} [-t {Target path}]\n" \
                    + "PROGRAM SPECIFICATION:\n" \
                    + "  A name of satellite observation program, ex:\n" \
                    + "    - Landsat\n    - Modis\n"\
                    + "PRODUCT:\n" \
                    + "  The image code to download, ex:\n" \
                    + "    - MOD11A1.005\n" \
                    + "REGION:\n" \
                    + "  A name of specific region to clip in image, ex:\n" \
                    + "    - Brasil\n" \
                    + "START DATE:\n" \
                    + "  The start date of image that will be download, ex:\n" \
                    + "    - 2014-01-01 (format YYYY-MM-DD)\n" \
                    + "END DATE:\n" \
                    + "  The end date of images that will be download, ex:\n" \
                    + "    - 2014-01-31 (format YYYY-MM-DD)\n" \
                    + "TARGET PATH:\n" \
                    + "  The path to folder where the files will be stored\n" \
                    + "    - ~/Maps (default path)")

def mapDict(argv):
    """This function get the arguments by parameters and put all
    system arguments in a dict variable considering the description
    of usage"""
    map = {}

    for i in range(len(argv)):
        if argv[i] == "-d": # program specification
            try:
                map["-d"] = argv[i + 1]
            except:
                print_usage(argv)
        elif argv[i] == "-p": # product
            try:
                map["-p"] = argv[i + 1]
            except:
                print_usage(argv)
        elif argv[i] == "-r": # region
            try:
                map["-r"] = argv[i + 1]
            except:
                print_usage(argv)
        elif argv[i] == "-s": # start date
            try:
                map["-s"] = argv[i + 1]
            except:
                print_usage(argv)
        elif argv[i] == "-e": # end date
            try:
                map["-e"] = argv[i + 1]
            except:
                print_usage(argv)
        elif argv[i] == "-t": # target path
            try:
                map["-t"] = argv[i + 1]
            except:
                print_usage(argv)

    return map

def main(argv):
    args_dict = mapDict(argv)

    if "-d" not in args_dict or "-p" not in args_dict or "-s" not in args_dict \
            or "-e" not in args_dict or "-r" not in args_dict:
        print_usage(argv)
    else:
        if args_dict["-d"].upper() == "MODIS":
            imgDownload = DownloadModis(product=args_dict["-p"],
                    name=args_dict["-r"], start=args_dict["-s"],
                    end=args_dict["-e"])
        elif args_dict["-d"].upper() == "LANDSAT":
            imgDownload = DownloadLandsat(product=args_dict["-p"],
                    name=args_dict["-r"], start=args_dict["-s"],
                    end=args_dict["-e"])


        if "-t" in args_dict:
            imgDownload.target = args_dict["-t"]

        imgDownload.run()

if __name__ == "__main__":
    main(sys.argv)
