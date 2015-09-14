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

def mosaic(targetPath = createDefaultPath()):
    baseKey = "REPROJECT_*"

    print("[MOSAIC MODULE   ]--> Start reading redis database...")

    conn = createConnection()

    while True:
        lKeys = conn.keys(pattern = baseKey)

        archDict = None
        if len(lKeys):
            lKeys.sort()

            key = lKeys[0]

            try:
                # get the content of the first key
                jsonTxt = conn.get(key)
            except:
                exit("[MOSAIC MODULE   ] |-> Problem with redis connection")

            try:
                # delete the first key
                conn.delete(key)
            except:
                exit("[MOSAIC MODULE   ] |-> Problem with redis connection")

            try:
                # convert json text to python dictionary
                archDict = json.loads(jsonTxt)
            except:
                print("[MOSAIC MODULE   ] |-> The value of key %s" % key \
                        + " have a bad format")

        if archDict is not None:
            print("[MOSAIC MODULE   ] |-> Mosaic requisition founded...")

            mosaic = MosaicImage(program=archDict["program"],
                    product=archDict["product"], region=archDict["region"],
                    startDate=archDict["startDate"],
                    endDate=archDict["endDate"],
                    bands_archive_list=archDict["bands"],
                    formula=archDict["formula"],
                    default_path=archDict["defaultPath"])

            if mosaic.run():
                print "[MOSAIC MODULE   ] |-> Finish mosaic conversation"
            else:
                print "[MOSAIC MODULE   ] |-> Impossible to create the mosaic"

        sleep(3)
