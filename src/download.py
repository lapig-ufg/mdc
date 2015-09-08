#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
from sys import argv
from downloadModis import DownloadModis
from downloadLandsat import DownloadLandsat
from common import mapDict
from common import createDefaultPath

def download(program, product, region, startDate, endDate,
        default_path = createDefaultPath()):
    if program and product and region and startDate and endDate:
        if program.upper() == "MODIS":
            imgDownload = DownloadModis(product=product,
                    region=region, start=startDate,
                    end=endDate, default_path=default_path)
        elif program.upper() == "LANDSAT":
            imgDownload = DownloadLandsat(product=product,
                    region=region, start=startDate,
                    end=endDate, default_path=default_path)
        else:
            return False

        if imgDownload.run() == True:
            print "[DOWNLOAD MODULE ]--> Finish download module"
        else:
            print "[DOWNLOAD MODULE ]--> Was not possible to make the download"

        return True
