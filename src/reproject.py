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
import json
import os
from time import sleep
from dbServer import createConnection
from modis import Modis

home_path = os.path.expanduser("~")
default_path = os.path.join(home_path, "Maps")
default_path = os.path.join(default_path, "downloaded")

def print_usage(args):
    #Print usage and exit
    sys.exit("Usage: %s -d {Program Specification} -p {Product} " %
            args[0] \
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

def convert(files):
    for file in files:
        file_path = os.path.join(default_path, file)

        print file_path

def main(args):
    args_dict = mapDict(args)

    if "-d" not in args_dict or "-p" not in args_dict:
        print_usage(args)
    else:
        if args_dict["-d"].upper() == "MODIS":
            baseKey = "MODIS_"

            product = Modis(args_dict["-p"])
        elif args_dict["-d"].upper() == "LANDSAT":
            baseKey = "LANDSAT_"

            sys.exit("Landsat was not implemented yet.")
        else:
            print_usage(args)


        if(product.exist):
            baseKey += product.product + '*'

            while(True):
                conn = createConnection()

                lKeys = conn.keys(pattern=baseKey)
                lKeys.sort()

                archDict = None
                for key in lKeys:
                    try:
                        jsonTxt = conn.get(key)
                    except:
                        sys.exit(" |-> Problem with redis connection")

                    try:
                        conn.delete(key)
                    except:
                        sys.exit(" |-> Problem with redis connection")

                    try:
                        archDict = json.loads(jsonTxt)
                        break
                    except:
                        print(" |-> The value of key %s have a bad format" %
                                key)

                if archDict != None:
                    convert(archDict["archives"])

                sleep(3)
        else:
            print_usage(args)

if __name__ == "__main__":
    main(sys.argv)
