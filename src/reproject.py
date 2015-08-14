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
        if args[i] == "-t": # target path
            try:
                argd["-t"] = args[i + 1]
            except:
                print_usage()

    return argd

def main(args):
    args_dict = mapDict(args)

    baseKey = "DOWNLOAD_MODIS_*"

    print("--> Start reading redis database...")
    while(True):
        conn = createConnection()

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

            if "-t" in args_dict:
                convertPrt.default_path = args_dict["-t"]

            convertPrt.run()

        sleep(3)

if __name__ == "__main__":
    main(sys.argv)
