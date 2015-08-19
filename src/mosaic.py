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
from sys import argv
from commun import mapDict
from dbServer import createConnection

usage = """\
Usage: %s [OPTIONS]
    [-t]    path to directory where the files will be stored
""" % argv[0]

def main():
    args_dict = mapDict(argv, usage)

    baseKey = "REPROJECT_*"

    print("--> Start reading redis database...")

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
                exit(" |-> Problem with redis connection")

            try:
                # delete the first key
                conn.delete(key)
            except:
                exit(" |-> Problem with redis connection")

            try:
                # convert json text to python dictionary
                archDict = json.loads(jsonTxt)
            except:
                print(" |-> The value of key %s have a bad format" %
                        key)

        if archDict is not None:
            print(" |-> Mosaic requisition founded...")

        sleep(3)

if __name__ == "__main__":
    main()
