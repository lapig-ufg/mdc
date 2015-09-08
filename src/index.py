#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
from common import createDefaultPath
from dbServer import createConnection

def index(formula, targetPath = createDefaultPath()):
    baseKey = "CLIP_*"

    print "[INDEX MODULE]--> Start reading redis database..."

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
                exit("[INDEX MODULE     ] |-> Problem with redis connection: " \
                        + e)

            try:
#                # delete the first key
                conn.delete(key)
            except Exception as e:
                exit("[INDEX MODULE     ] |-> Problem with redis connection: " \
                        + e)

            try:
                # convert json text to python dictionary
                archDict = json.loads(jsonTxt)
            except Exception as e:
                print("[INDEX MODULE     ] |-> The value of key %s " % key \
                    + " have a bad format: " + e)

        if archDict is not None:
            print("[INDEX MODULE     ] |-> Clip requisition founded...")

            keyAux = key.split('_')
            program = keyAux[1]
            product = keyAux[2]
            startDate = keyAux[3]
            endDate = keyAux[4]
