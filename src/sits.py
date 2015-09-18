#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import time
import datetime
import json
from sys import platform
from sys import exit
from subprocess import Popen
from sys import argv
from os import path
from common import mapDict
from common import createDefaultPath
from common import createMrtPath
from dbServer import createConnection

usage = """\
Usage: %s [OPTIONS]
    -d      name of satellite observation program
    -p      product name
    -r      download specifics tiles of this region
    -s      start date of image that will be download
    -e      end date of images that will be download
    -i      index formula to apply
    [-t]    path to directory where the files will be stored
    [-m]    mrt path
""" % argv[0]

conn = createConnection()

def writeArgsToRedis(program, product, region, startDate, endDate, index,
        default_path=createDefaultPath(), mrt_path=createMrtPath()):

    contentJson = json.dumps({
            "program" : program,
            "product" : product,
            "region" : region,
            "startDate" : startDate,
            "endDate" : endDate,
            "index" : index,
            "defaultPath" : default_path,
            "mrtPath" : mrt_path
            })

    dt = datetime.datetime.fromtimestamp(time.time()).strftime(
            "%Y-%m-%d_%H:%M:%S")
    key = "SITS_ARGS_" + dt

    try:
        conn.set(key, contentJson)
    except:
        exit("[SITS ] |-> Error: Problem with redis " \
                + "database connection...")

def writePidToRedis(module, pid):
    key = "SITS_PID_" + module

    try:
        conn.set(key, pid)
    except:
        print("[SITS] |-> Error: Was not possible to write %s pid to "
                % module + "redis database")

def procExists(module):
    key = "SITS_PID_" + module

    try:
        pid = conn.get(key)

        if pid == None:
            return False

    except:
        print("[SITS] |-> Error: Was not possible to read %s pid to "
                % module + "redis database")

        return False

    # Verificar se isso pode ser usado no MAC também
    # Criar um mecanismo de verificação para RUindows
    if platform.find("linux") == 0:
        if path.exists("/proc/" + pid):
            return True

    return False

def main():
    print "[SITS]--------------> Starting satellite image time series..."

    argDict = mapDict(argv, usage)
    basePath = path.dirname(path.abspath(__file__))

    if "-d" in argDict and "-p" in argDict and "-r" in argDict \
            and "-s" in argDict and "-e" in argDict and "-i" in argDict:

        if "-t" in argDict:
            default_path = argDict["-t"]
        else:
            default_path = createDefaultPath()

        if "-m" in argDict:
            mrt_path = argDict["-m"]
        else:
            mrt_path = createMrtPath()

        writeArgsToRedis(program=argDict["-d"], product=argDict["-p"],
                region=argDict["-r"], startDate=argDict["-s"],
                endDate=argDict["-e"], index=argDict["-i"],
                default_path=default_path, mrt_path=mrt_path)

        if not procExists("download"):
            try:
                download_path = path.join(basePath, "download.py")
                p = Popen(["python", download_path, ">", "../download.log"])
                writePidToRedis("download", p.pid)
            except OSError:
                print "[SITS] |-> %s does not exist." % download_path
        else:
            print "[SITS] |-> Download module aready running"

        if not procExists("reproject"):
            try:
                reproject_path = path.join(basePath, "reproject.py")
                p = Popen(["python", reproject_path])
                writePidToRedis("reproject", p.pid)
            except OSError:
                print "[SITS] |-> %s does not exist." % reproject_path
        else:
            print "[SITS] |-> Reproject module aready running"

        if not procExists("mosaic"):
            try:
                mosaic_path = path.join(basePath, "mosaic.py")
                p = Popen(["python", mosaic_path])
                writePidToRedis("mosaic", p.pid)
            except OSError:
                print "[SITS] |-> %s does not exist." % mosaic_path
        else:
            print "[SITS] |-> Mosaic module aready running"

        if not procExists("clip"):
            try:
                clip_path = path.join(basePath, "clip.py")
                p = Popen(["python", clip_path])
                writePidToRedis("clip", p.pid)
            except OSError:
                print "[SITS] |-> %s does not exist." % clip_path
        else:
            print "[SITS] |-> Clip module aready running"

        if not procExists("index"):
            try:
                index_path = path.join(basePath, "index.py")
                p = Popen(["python", index_path])
                writePidToRedis("index", p.pid)
            except OSError:
                print "[SITS] |-> %s does not exist." % reproject_path
        else:
            print "[SITS] |-> Index module aready running"
    else:
        exit(usage)

if __name__ == "__main__":
    main()
