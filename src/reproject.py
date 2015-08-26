#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import json
from sys import exit
from sys import argv
from time import sleep
from dbServer import createConnection
from modis import Modis
from convert import convert
from common import mapDict
from common import createDefaultPath

def reproject(targetPath = createDefaultPath()):
    # make the pattern key to search in redis
    baseKey = "DOWNLOAD_MODIS_*"

    print("--> Start reading redis database...")

    # repeat this
    while(True):
        conn = createConnection()

        # search the database by pattern key
        lKeys = conn.keys(pattern=baseKey)
        # sort list keys
        lKeys.sort()

        archDict = None
        # if have one or more key
        if len(lKeys):
            key = lKeys[0]

            try:
                # get the content of the first key
                jsonTxt = conn.get(key)
            except:
                exit(" |-> Problem with redis connection")

            try:
                # delete the first key
                conn.delete(key)
            except:
                exit(" |-> Problem with redis connection")

            try:
                # convert json text to python dictionary
                archDict = json.loads(jsonTxt)
            except:
                print(" |-> The value of key %s have a bad format" %
                        key)

        # if have content
        if archDict != None:
            print(" |-> Convert requisition founded...")

            startDate = key.split('_')[-2]
            endDate = key.split('_')[-1]

            # create a object of specific product and list of archives
            convertPrt = convert(product=archDict["product"],
                    archive_list=archDict["archives"], start_date=startDate,
                    end_date=endDate, default_path=targetPath)

            # convert all archives of specific list
            convertPrt.run()

        # wait 3 seconds
        sleep(3)


usage = """\
Usage: %s [OPTIONS]
    [-t]    path to directory where the files will be stored
""" % argv[0]

"""
def main():
    args_dict = mapDict(argv, usage)

    # make the pattern key to search in redis
    baseKey = "DOWNLOAD_MODIS_*"

    print("--> Start reading redis database...")

    # repeat this
    while(True):
        conn = createConnection()

        # search the database by pattern key
        lKeys = conn.keys(pattern=baseKey)
        # sort list keys
        lKeys.sort()

        archDict = None
        # if have one or more key
        if len(lKeys):
            key = lKeys[0]

            try:
                # get the content of the first key
                jsonTxt = conn.get(key)
            except:
                exit(" |-> Problem with redis connection")

            try:
                # delete the first key
                conn.delete(key)
            except:
                exit(" |-> Problem with redis connection")

            try:
                # convert json text to python dictionary
                archDict = json.loads(jsonTxt)
            except:
                print(" |-> The value of key %s have a bad format" %
                        key)

        # if have content
        if archDict != None:
            print(" |-> Convert requisition founded...")

            startDate = key.split('_')[-2]
            endDate = key.split('_')[-1]

            # create a object of specific product and list of archives
            convertPrt = convert(archDict["product"], archDict["archives"],
                    startDate, endDate)

            # if have a diferent work path of the default change the attribute
            if "-t" in args_dict:
                convertPrt.default_path = args_dict["-t"]

            # convert all archives of specific list
            convertPrt.run()

        # wait 3 seconds
        sleep(3)

if __name__ == "__main__":
    main()
"""
