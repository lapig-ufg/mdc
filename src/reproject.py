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
from os import path
from sys import exit
from time import sleep
from dbServer import createConnection
from modis import Modis
from convert import convert
from common import mapDict
from common import createDefaultPath

def createMrtPath():
    """ Function which create a string of $HOME/.mrt path """

    home_path = path.expanduser("~")
    mrt_path = path.join(home_path, ".mrt")
    return mrt_path


def reproject(default_path = createDefaultPath(), mrt_path = createMrtPath()):
    # make the pattern key to search in redis
    baseKey = "DOWNLOAD_MODIS_*"

    print("[REPROJECT MODULE]--> Start reading redis database...")

    # repeat this
    while(True):
        conn = createConnection()

        # search the database by pattern key
        lKeys = conn.keys(pattern=baseKey)
        # sort list keys
        lKeys.sort()

        archDict = None
        # if have one or more key
        if len(lKeys):
            key = lKeys[0]

            try:
                # get the content of the first key
                jsonTxt = conn.get(key)
            except:
                exit("[REPROJECT MODULE] |-> Problem with redis connection")

            try:
                # delete the first key
                conn.delete(key)
            except:
                exit("[REPROJECT MODULE] |-> Problem with redis connection")

            try:
                # convert json text to python dictionary
                archDict = json.loads(jsonTxt)
            except:
                print("[REPROJECT MODULE] |-> The value of key %s have a bad " \
                        + "format" % key)

        # if have content
        if archDict != None:
            print("[REPROJECT MODULE] |-> Convert requisition founded...")

            startDate = key.split('_')[-2]
            endDate = key.split('_')[-1]

            # create a object of specific product and list of archives
            convertPrt = convert(product=archDict["product"],
                    archive_list=archDict["archives"], start_date=startDate,
                    end_date=endDate, default_path=default_path,
                    mrt_path=mrt_path)

            # convert all archives of specific list
            if convertPrt.run():
                print "[REPROJECT MODULE] |-> Finish convert module"
            else:
                print "[REPROJECT MODULE] |-> Problem wich convert module"

        # wait 3 seconds
        sleep(3)
