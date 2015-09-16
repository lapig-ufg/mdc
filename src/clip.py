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

def main():
    baseKey = "MOSAIC_*"

    print "[CLIP MODULE]-------> Start reading redis database..."

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
            except Exception as e:
                exit("[CLIP MODULE] |-> Problem with redis connection: " \
                        + e)

            try:
#                # delete the first key
                conn.delete(key)
            except Exception as e:
                exit("[CLIP MODULE] |-> Problem with redis connection: " \
                        + e)

            try:
                # convert json text to python dictionary
                contentDict = json.loads(jsonTxt)
            except Exception as e:
                print("[CLIP MODULE] |-> The value of key %s " % key \
                    + " have a bad format: " + e)

        if contentDict is not None:
            print("[CLIP MODULE] |-> Clip requisition founded...")

            clip = ClipImage(product=contentDict["product"],
                    program=contentDict["program"],
                    region=contentDict["region"],
                    archive_list=contentDict["archives"],
                    startDate=contentDict["startDate"],
                    endDate=contentDict["endDate"],
                    formula=contentDict["formula"],
                    default_path=contentDict["defaultPath"])

            if clip.run():
                print("[CLIP MODULE] |-> Finish clip image")
            else:
                print("[CLIP MODULE] |-> Impossible to clip image")

            sleep(3)

if __name__ == "__main__":
    main()
