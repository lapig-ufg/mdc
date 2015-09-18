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
from indexImage import indexImage
from common import createDefaultPath
from dbServer import createConnection

def main():
    baseKey = "CLIP_*"

    print "[INDEX MODULE]------> Start reading redis database..."

    conn = createConnection()

#    while True:
    lKeys = conn.keys(pattern = baseKey)

    contentDict = None
    if len(lKeys):
        lKeys.sort()
        key = lKeys[0]

        try:
            # get the content of the first key
            jsonTxt = conn.get(key)
        except Exception as e:
            exit("[INDEX MODULE] |-> Problem with redis connection: " \
                    + e)

#        try:
#                # delete the first key
#            conn.delete(key)
#        except Exception as e:
#            exit("[INDEX MODULE] |-> Problem with redis connection: " \
#                    + e)

        try:
            # convert json text to python dictionary
            contentDict = json.loads(jsonTxt)
        except Exception as e:
            print("[INDEX MODULE] |-> The value of key %s " % key \
                + " have a bad format: " + e)

    if contentDict is not None:
        print("[INDEX MODULE] |-> Clip requisition founded...")

        index = indexImage(program=contentDict["program"],
                product=contentDict["product"],
                archives_list=contentDict["archives"],
                formula=contentDict["formula"],
                startDate=contentDict["startDate"],
                endDate=contentDict["endDate"],
                region=contentDict["region"],
                default_path=contentDict["defaultPath"])

        if index.run():
            print "[INDEX MODULE] |-> Finish index process"
        else:
            print "[INDEX MODULE] |-> Impossible to apply index " \
                    + "process"

    sleep(3)

if __name__ == "__main__":
    main()
