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
from time import sleep
from dbServer import createConnection
from modis import Modis

def print_usage(args):
    #Print usage and exit
    sys.exit("Usage: %s -d {Program Specification} -p {Product} " %
            argv[0] \
                    + "[-t {Target path}]\n" \
                    + "PROGRAM SPECIFICATION:\n" \
                    + "  A name of satellite observation program, ex:\n" \
                    + "    - Landsat\n    - Modis\n"\
                    + "PRODUCT:\n" \
                    + "  The image code to download, ex:\n" \
                    + "    - MOD11A1.005\n" \
                    + "TARGET PATH:\n" \
                    + "  The path to folder where the files will be stored\n" \
                    + "    - ~/Maps (default path)")

def mapDict(args):
    """This function get the arguments by parameters and put all
        system arguments in a dict variable considering the description
        of usage
    """
    argd = {}

    for i in range(len(args)):
        if args[i] == "-d": # program specification
            try:
                argd["-d"] = args[i + 1]
            except:
                print_usage(args)
        elif args[i] == "-p": # product
            try:
                argd["-p"] = args[i + 1]
            except:
                print_usage(args)
        elif args[i] == "-t": # target path
            try:
                argd["-t"] = args[i + 1]
            except:
                print_usage(args)

    return argd

def main(args):
    argDict = mapDict(args)

    if "-d" not in args_dict or "-p":
        print_usage(args)
    else:
        if argDict["-d"].upper() == "MODIS":
            baseKey = "MODIS_"
        elif argDict["-d"].upper() == "LANDSAT":
            baseKey = "LANDSAT_"
        else:
            print_usage(args)

        modis = Modis(argDict["-p"])

        if(modis.exists):
            while(True):
                conn = createConnection()

                sleep(10)
        else:
            print_usage(args)

if __name__ == "__main__":
    mains(sys.args)
