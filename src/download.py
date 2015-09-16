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
from time import sleep
from downloadModis import DownloadModis
from downloadLandsat import DownloadLandsat
from dbServer import createConnection

def main():
    # make the pattern key to search in redis
    baseKey = "SITS_ARGS_*"

    print("[DOWNLOAD MODULE]--> Start reading redis database...")

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
                exit("[DOWNLOAD MODULE] |-> Problem with redis connection")

            try:
                # delete the first key
                conn.delete(key)
            except:
                exit("[DOWNLOAD MODULE] |-> Problem with redis connection")

            try:
                # convert json text to python dictionary
                contentDict = json.loads(jsonTxt)
            except:
                print("[DOWNLOAD MODULE] |-> The value of key %s have a bad "
                        % key + "format")

        # if have content
        if contentDict != None:
            print("[DOWNLOAD MODULE] |-> Download requisition founded...")

            if contentDict["program"].upper() == "MODIS":
                imgDownload = DownloadModis(product=contentDict["product"],
                    region=contentDict["region"],
                    start=contentDict["startDate"],
                    end=contentDict["endDate"],
                    formula=contentDict["index"],
                    default_path=contentDict["defaultPath"],
                    mrt_path=contentDict["mrtPath"])

            elif archDict["program"].upper() == "LANDSAT":
                imgDownload = DownloadLandsat(product=contentDict["product"],
                    region=contentDict["region"],
                    start=contentDict["startDate"],
                    end=contentDict["endDate"],
                    formula=contentDict["index"],
                    default_path=contentDict["defaultPath"],
                    mrt_path=contentDict["mrtPath"])

            if imgDownload.run() == True:
                print "[DOWNLOAD MODULE]--> Finish download module"
            else:
                print "[DOWNLOAD MODULE]--> Was not possible to make the download"

        sleep(3)

if __name__ == "__main__":
    main()
