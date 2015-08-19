#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import datetime

class Modis:
    """ A class which define the modis product data """

    def __init__(self, product):
        self.product = product
        self.__generateModis()

    def __createLayers(self, name):
        listLayers = []

        if name == "MOD09A1.005":
            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "4294967295" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "65535" })

            listLayers.append({ "fill" : "65535" })

        elif name == "MOD09CMG.005":
            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD09GA.005":
            listLayers.append({ "fill" : "-1" })

            listLayers.append({ "fill" : "65535" })

            listLayers.append({ "fill" : "-32767" })

            listLayers.append({ "fill" : "-32767" })

            listLayers.append({ "fill" : "65535" })

            listLayers.append({ "fill" : "-32767" })

            listLayers.append({ "fill" : "-32767" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "-1" })

            listLayers.append({ "fill" : "-1" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "787410671" })

            listLayers.append({ "fill" : "-1" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

        elif name == "MOD09GQ.005":
            listLayers.append({ "fill" : "-1" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "2995" })

            listLayers.append({ "fill" : "-1" })

        elif name == "MOD09Q1.005":
            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "-28672" })

            listLayers.append({ "fill" : "65535" })

        elif name == "MOD11_L2.004" or name == "MOD11_L2.041":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "-999" })

            listLayers.append({ "fill" : "-999" })

        elif name == "MOD11_L2.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "-999" })

            listLayers.append({ "fill" : "-999" })

        elif name == "MOD11A1.004" or name == "MOD11A1.041":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD11A1.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD11A2.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" }) # See QA NOTE

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" }) # See QA NOTE

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD11B1.004" or name == "MOD11B1.041":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD11B1.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD11C1.004" or name == "MOD11C1.041":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD11C1.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD11C2.004" or name == "MOD11C2.041":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD11C2.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD11C3.004" or name == "MOD11C3.041":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

        elif name ==" MOD11C3.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD13A1.005":
            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "65535" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-10000" })

            listLayers.append({ "fill" : "-10000" })

            listLayers.append({ "fill" : "-4000" })

            listLayers.append({ "fill" : "-1" })

            listLayers.append({ "fill" : "-1" })

        elif name == "MOD13A2.005":
            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "65535" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-10000" })

            listLayers.append({ "fill" : "-10000" })

            listLayers.append({ "fill" : "-4000" })

            listLayers.append({ "fill" : "-1" })

            listLayers.append({ "fill" : "-1" })

        elif name == "MOD13A3":
            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "65535" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-10000" })

            listLayers.append({ "fill" : "-10000" })

            listLayers.append({ "fill" : "-4000" })

            listLayers.append({ "fill" : "-1" })


        return listLayers

    def __generateModis(self):
        self.exist = True

        if self.product.upper() == "MOD09A1.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 13
            self.layers = self.__createLayers("MOD09A1.005")

        elif self.product.upper() == "MOD09CMG.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 21

        elif self.product.upper() == "MOD09GA.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 21

        elif self.product.upper() == "MOD09GQ.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 5

        elif self.product.upper() == "MOD09Q1.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 3

        elif self.product.upper() == "MOD11A1.004":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2007-01-03",
                    "%Y-%m-%d")
            self.nBand = 12

        elif self.product.upper() == "MOD11A1.041":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 12

        elif self.product.upper() == "MOD11A1.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 12

        elif self.product.upper() == "MOD11A2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 12

        elif self.product.upper() == "MOD11B1.004":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2007-01-04",
                    "%Y-%m-%d")
            self.nBand = 17

        elif self.product.upper() == "MOD11B1.041":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 17

        elif self.product.upper() == "MOD11B1.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 18

        elif self.product.upper() == "MOD11C1.004":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2007-01-03",
                    "%Y-%m-%d")
            self.nBand = 15

        elif self.product.upper() == "MOD11C1.041":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 15

        elif self.product.upper() == "MOD11C1.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 16

        elif self.product.upper() == "MOD11C2.004":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2006-12-31",
                    "%Y-%m-%d")
            self.nBand = 15

        elif self.product.upper() == "MOD11C2.041":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 15

        elif self.product.upper() == "MOD11C2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 17

        elif self.product.upper() == "MOD11C3.004":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2006-12-31",
                    "%Y-%m-%d")
            self.nBand = 16

        elif self.product.upper() == "MOD11C3.041":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 16

        elif self.product.upper() == "MOD11C3.005":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 17

        elif self.product.upper() == "MOD11_L2.004":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2007-01-03",
                    "%Y-%m-%d")
            self.nBand = 9

        elif self.product.upper() == "MOD11_L2.041":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 9

        elif self.product.upper() == "MOD11_L2.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 9

        elif self.product.upper() == "MOD13A1.005":
            self.temporalColect = 16
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 12

        elif self.product.upper() == "MOD13A2.005":
            self.temporalColect = 16
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 12

        elif self.product.upper() == "MOD13A3":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 11

        elif self.product.upper() == "MOD13C1.005":
            self.temporalColect = 16
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 13

        elif self.product.upper() == "MOD13C2.005":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 13

        elif self.product.upper() == "MOD13Q1.005":
            self.temporalColect = 16
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 12

        elif self.product.upper() == "MOD14.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 23

        elif self.product.upper() == "MOD14A1.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 5

        elif self.product.upper() == "MOD14A2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 2

        elif self.product.upper() == "MOD15A2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 6

        elif self.product.upper() == "MOD17A2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None
            self.nBand = 3

        elif self.product.upper() == "MOD17A3.055":
            self.temporalColect = 365
            self.initDateProgram = datetime.datetime.strptime("2000-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2010-12-31",
                    "%Y-%m-%d")
            self.nBand = 3

        elif self.product.upper() == "MOD44A.004":
            self.temporalColect = 365
            self.initDateProgram = datetime.datetime.strptime("2002-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2002-12-31",
                    "%Y-%m-%d")
            self.nBand = 4

        elif self.product.upper() == "MOD44B.005":
            self.temporalColect = 365
            self.initDateProgram = datetime.datetime.strptime("2000-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2010-12-31",
                    "%Y-%m-%d")
            self.nBand = 4

        elif self.product.upper() == "MOD44B.051":
            self.temporalColect = 365
            self.initDateProgram = datetime.datetime.strptime("2000-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2013-12-31",
                    "%Y-%m-%d")
            self.nBand = 7

        elif self.product.upper() == "MOD44W.005":
            self.temporalColect = 365
            self.initDateProgram = None
            self.endDateProgram = None
            self.nBand = 2

        else:
            self.temporalColect = None
            self.initDateProgram = None
            self.endDateProgram = None
            self.nBand = None
            self.exist = False
