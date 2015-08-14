#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import sys
from downloadModis import DownloadModis
from downloadLandsat import DownloadLandsat

usage = """\
Usage: %s [OPTIONS]
    -d      name of satellite observation program
    -p      product name
    -r      download specifics tiles of this region
    -s      start date of image that will be download
    -e      end date of images that will be download
    [-t]    path to directory where the files will be stored
""" % sys.argv[0]

def print_usage(usage_txt = usage):
    #Print usage and exit
    sys.exit(usage_txt)

def mapDict(argv):
    """This function get the arguments by parameters and put all
        system arguments in a dict variable considering the description
        of usage
    """
    map = {}

    for i in range(len(argv)):
        if argv[i] == "-d": # program specification
            try:
                map["-d"] = argv[i + 1]
            except:
                print_usage()
        elif argv[i] == "-p": # product
            try:
                map["-p"] = argv[i + 1]
            except:
                print_usage()
        elif argv[i] == "-r": # region
            try:
                map["-r"] = argv[i + 1]
            except:
                print_usage()
        elif argv[i] == "-s": # start date
            try:
                map["-s"] = argv[i + 1]
            except:
                print_usage()
        elif argv[i] == "-e": # end date
            try:
                map["-e"] = argv[i + 1]
            except:
                print_usage()
        elif argv[i] == "-t": # target path
            try:
                map["-t"] = argv[i + 1]
            except:
                print_usage()

    return map

def main(argv):
    args_dict = mapDict(argv)

    if "-d" not in args_dict or "-p" not in args_dict or "-s" not in args_dict \
            or "-e" not in args_dict or "-r" not in args_dict:
        print_usage()
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
            print_usage()

        if "-t" in args_dict:
            imgDownload.target = args_dict["-t"]

        if imgDownload.run() == True:
            print "--> Finish download module"
        else:
            print "--> Was not possible to make the download"

if __name__ == "__main__":
    main(sys.argv)
