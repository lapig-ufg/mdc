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
from os import path
from sys import exit
from time import sleep
from dbServer import createConnection
from modis import Modis
from reprojectImage import reprojectImage
from common import mapDict
from common import createDefaultPath

def main():
    # make the pattern key to search in redis
    baseKey = "DOWNLOAD_MODIS_*"

    print("[REPROJECT MODULE]--> Start reading redis database...")

    conn = createConnection()

    # repeat this
    while(True):
        # search the database by pattern key
        lKeys = conn.keys(pattern=baseKey)

        contentDict = None
        # if have one or more key
        if len(lKeys):
            # sort list keys
            lKeys.sort()

            key = lKeys[0]

            try:
                # get the content of the first key
                jsonTxt = conn.get(key)
            except:
                exit("[REPROJECT MODULE] |-> Problem with redis connection")

            try:
                # delete the first key
                conn.delete(key)
            except:
                exit("[REPROJECT MODULE] |-> Problem with redis connection")

            try:
                # convert json text to python dictionary
                contentDict = json.loads(jsonTxt)
            except:
                print("[REPROJECT MODULE] |-> The value of key %s have a bad " \
                        + "format" % key)

        # if have content
        if contentDict != None:
            print("[REPROJECT MODULE] |-> Convert requisition founded...")

            # create a object of specific product and list of archives
            convertPrt = reprojectImage(program=contentDict["program"],
                    product=contentDict["product"],
                    region=contentDict["region"],
                    start_date=contentDict["startDate"],
                    end_date=contentDict["endDate"],
                    default_path=contentDict["defaultPath"],
                    archive_list=contentDict["archives"],
                    formula=contentDict["formula"],
                    mrt_path=contentDict["mrtPath"])

            # convert all archives of specific list
            if convertPrt.run():
                print "[REPROJECT MODULE] |-> Finish convert module"
            else:
                print "[REPROJECT MODULE] |-> Problem wich convert module"

        # wait 3 seconds
        sleep(3)

if __name__ == "__main__":
    main()
