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
from common import mapDict
from common import createDefaultPath
from mosaicImage import MosaicImage
from dbServer import createConnection

def mosaic(targetPath = createDefaultPath()):
    baseKey = "REPROJECT_*"

    print("[MOSAIC MODULE]--> Start reading redis database...")

    while(True):
        conn = createConnection()

        lKeys = conn.keys(pattern = baseKey)
        lKeys.sort()

        archDict = None
        if len(lKeys):
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
                archDict = json.loads(jsonTxt)
            except:
                print("[MOSAIC MODULE] |-> The value of key %s have a bad " \
                        + "format" % key)

        if archDict is not None:
            print("[MOSAIC MODULE] |-> Mosaic requisition founded...")

            keyAux = key.split('_')
            program = keyAux[1]
            product = keyAux[2]
            startDate = keyAux[3]
            endDate = keyAux[4]

            mosaic = MosaicImage(program=program, product=product,
                    bands_archive_list=archDict, startDate=startDate,
                    endDate=endDate, default_path=targetPath)

            if mosaic.run():
                print "[MOSAIC MODULE] |-> Finish mosaic conversation"
            else:
                print "[MOSAIC MODULE] |-> Impossible to create the mosaic"

        sleep(3)
