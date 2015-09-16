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
from time import sleep
from common import createDefaultPath
from clipImage import ClipImage
from dbServer import createConnection

def clip():
    baseKey = "MOSAIC_*"

    print "[CLIP MODULE     ]--> Start reading redis database..."

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
            except Exception as e:
                exit("[CLIP MODULE     ] |-> Problem with redis connection: " \
                        + e)

            try:
#                # delete the first key
                conn.delete(key)
            except Exception as e:
                exit("[CLIP MODULE     ] |-> Problem with redis connection: " \
                        + e)

            try:
                # convert json text to python dictionary
                archDict = json.loads(jsonTxt)
            except Exception as e:
                print("[CLIP MODULE     ] |-> The value of key %s " % key \
                    + " have a bad format: " + e)

        if archDict is not None:
            print("[CLIP MODULE     ] |-> Clip requisition founded...")

            clip = ClipImage(product=archDict["product"],
                    program=archDict["program"], region=archDict["region"],
                    archive_list=archDict["archives"],
                    startDate=archDict["startDate"],
                    endDate=archDict["endDate"],
                    formula=archDict["formula"],
                    default_path=archDict["defaultPath"])

            if clip.run():
                print("[CLIP MODULE     ] |-> Finish clip image")
            else:
                print("[CLIP MODULE     ] |-> Impossible to clip image")

            sleep(3)
