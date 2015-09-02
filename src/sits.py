#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
from multiprocessing import Process
from sys import argv
from common import mapDict
from download import download
from reproject import reproject
from mosaic import mosaic

usage = """\
Usage: %s [OPTIONS]
    -d      name of satellite observation program
    -p      product name
    -r      download specifics tiles of this region
    -s      start date of image that will be download
    -e      end date of images that will be download
    -i      index formula to apply
    [-t]    path to directory where the files will be stored
""" % argv[0]

def main():
    argDict = mapDict(argv, usage)

    if "-d" in argDict and "-p" in argDict and "-r" in argDict \
            and "-s" in argDict and "-e" in argDict and "-i" in argDict:

        downParams = [argDict["-d"], argDict["-p"], argDict["-r"],
                argDict["-s"], argDict["-e"]]

        repParams = []

        mosParams = []

        if "-t" in argDict:
            downParams.append(argDict["-t"])
            repParams.append(argDict["-t"])
            mosParams.append(argDict["-t"])

        pDown = Process(target=download, args=downParams)
        pDown.start()
#        pDown.join()

        pRepr = Process(target=reproject, args=repParams)
        pRepr.start()
#        pRepr.join()

        pMos = Process(target=mosaic, args=mosParams)
        pMos.start()
#        pMos.join()

    else:
        exit(usage)

if __name__ == "__main__":
    main()
