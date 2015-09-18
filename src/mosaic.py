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
from common import createDefaultPath
from mosaicImage import MosaicImage
from dbServer import createConnection

def main():
    baseKey = "REPROJECT_*"

    print "[MOSAIC MODULE]-----> Start reading redis database..."

    conn = createConnection()

    while True:
        lKeys = conn.keys(pattern = baseKey)

        contentDict = None
        if len(lKeys):
            lKeys.sort()

            key = lKeys[0]

            try:
                # get the content of the first key
                jsonTxt = conn.get(key)
            except:
                exit("[MOSAIC MODULE] |-> Problem with redis connection")

            try:
                # delete the first key
                conn.delete(key)
            except:
                exit("[MOSAIC MODULE] |-> Problem with redis connection")

            try:
                # convert json text to python dictionary
                contentDict = json.loads(jsonTxt)
            except:
                print("[MOSAIC MODULE] |-> The value of key %s" % key \
                        + " have a bad format")

        if contentDict is not None:
            print("[MOSAIC MODULE] |-> Mosaic requisition founded...")

            mosaic = MosaicImage(program=contentDict["program"],
                    product=contentDict["product"],
                    region=contentDict["region"],
                    startDate=contentDict["startDate"],
                    endDate=contentDict["endDate"],
                    bands_archive_list=contentDict["bands"],
                    formula=contentDict["formula"],
                    default_path=contentDict["defaultPath"])

            if mosaic.run():
                print "[MOSAIC MODULE] |-> Finish mosaic conversation"
            else:
                print "[MOSAIC MODULE] |-> Impossible to create the mosaic"

            sleep(3)

if __name__ == "__main__":
    main()
