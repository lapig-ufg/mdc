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
from convert import convert

usage = """\
Usage: %s [OPTIONS]
    -p      product name
    [-t]    path to directory where the files will be stored
""" % sys.argv[0]

def print_usage(usage_txt = usage):
    #Print usage and exit
    sys.exit(usage_txt)

def mapDict(args):
    """This function get the arguments by parameters and put all
        system arguments in a dict variable considering the description
        of usage
    """
    argd = {}

    for i in range(len(args)):
        if args[i] == "-p": # product
            try:
                argd["-p"] = args[i + 1]
            except:
                print_usage()
        elif args[i] == "-t": # target path
            try:
                argd["-t"] = args[i + 1]
            except:
                print_usage()

    return argd

def main(args):
    args_dict = mapDict(args)

    if "-p" not in args_dict:
        print_usage()
    else:
        baseKey = "MODIS_"

        product = Modis(args_dict["-p"])

        if(product.exist):
            baseKey += product.product + '*'

            if "-t" in args_dict:
                default_path = args_dict["-t"]

            while(True):
                conn = createConnection()

                print("--> Reading redis database...")
                lKeys = conn.keys(pattern=baseKey)
                lKeys.sort()

                archDict = None
                if len(lKeys):
                    try:
                        jsonTxt = conn.get(lKeys[0])
                    except:
                        sys.exit(" |-> Problem with redis connection")

                    try:
                        conn.delete(lKeys[0])
                    except:
                        sys.exit(" |-> Problem with redis connection")

                    try:
                        archDict = json.loads(jsonTxt)
                    except:
                        print(" |-> The value of key %s have a bad format" %
                                key)


                if archDict != None:
                    print(" |-> Convert requisition founded...")
                    convertPrt = convert(archDict["product"],
                            archDict["archives"])
                    convertPrt.run()

                sleep(3)
        else:
            print_usage()

if __name__ == "__main__":
    main(sys.argv)
