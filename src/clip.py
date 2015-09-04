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

def clip(region, targetPath = createDefaultPath()):
    baseKey = "MOSAIC_*"

    print "[CLIP MODULE     ]--> Start reading redis database..."

    while True:
        conn = createConnection()

        lKeys = conn.keys(pattern = baseKey)
        lKeys.sort()

        archDict = None
        if len(lKeys):
            key = lKeys[0]

            try:
                # get the content of the first key
                jsonTxt = conn.get(key)
            except Exception as e:
                exit("[CLIP MODULE     ] |-> Proble with redis connection: " \
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

            keyAux = key.split('_')
            program = keyAux[1]
            product = keyAux[2]
            startDate = keyAux[3]
            endDate = keyAux[4]

            clip = ClipImage(program, product, archDict["archives"], startDate,
                    endDate, region, targetPath)

            if clip.run():
                print("[CLIP MODULE     ] |-> Finish clip image")
            else:
                print("[CLIP MODULE     ] |-> Impossible to clip image")

            sleep(3)
