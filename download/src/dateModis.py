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
from sys import exit

class DateModis:
    """ A class to create an list of pair date determined by satellite image
        colect day
    """

    def __init__(self, product, startDate, endDate):
        self.product = product
        self.startDate = self.__convertDate(startDate)
        self.endDate = self.__convertDate(endDate)
        self.datesList = self.__makeDate(product, startDate, endDate)

    def __convertDate(self, strDate):
        try:
            return datetime.datetime.strptime(strDate, "%Y-%m-%d")
        except:
            exit("-> Error: '%s' have a wrong date format, use YYYY-MM-DD" %
                    strDate)

    def __makeDate(self, product, startDate, endDate):
        """ create a list of dates """

        dateList = []

        trColect = self.__getTemporalColect(product)

        start = self.startDate
        end = start

        # while the end date used to next date pair are less than endDate
        while end < self.endDate:
            # add the start date to colect day
            end = start + datetime.timedelta(days=trColect)

            # if the end date of next date pair is more than endDate use endDate
            if end > self.endDate:
                end = self.endDate

            # append an dict of start date and end date pair
            dateList.append({"start" : start.strftime("%Y-%m-%d"),
                "end" : end.strftime("%Y-%m-%d")})

            # add 1 day to end date and put into start date
            # start = end + datetime.timedelta(days=1)
            start = end


        return dateList

    def __getTemporalColect(self, product):
        # define a colect day of modis product
        if product.upper() == "MOD09A1.005":
            colect = 8
            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD09CMG.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD09GA.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD09GQ.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD09Q1.005":
            colect = 8

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11A1.004":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2007-01-03", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD11A1.041":
            colect = 1

            startDtClt = datetime.datetime.strptime("2007-01-01", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11A1.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11A2.005":
            colect = 8

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11B1.004":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2007-01-04", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD11B1.041":
            colect = 1

            startDtClt = datetime.datetime.strptime("2007-01-01", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11B1.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11B1.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2007-01-03", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD11B1.041":
            colect = 1

            startDtClt = datetime.datetime.strptime("2007-01-01", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11B1.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11C2.004":
            colect = 8

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2006-12-31", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD11C2.041":
            colect = 8

            startDtClt = datetime.datetime.strptime("2007-01-01", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11C2.005":
            colect = 8

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11C3.004":
            colect = 30

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2006-12-31", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD11C3.041":
            colect = 30

            startDtClt = datetime.datetime.strptime("2007-01-01", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11C3.005":
            colect = 30

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11_L2.004":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2007-01-03", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD11_L2.041":
            colect = 1

            startDtClt = datetime.datetime.strptime("2007-01-01", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD11_L2.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-03-05", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD13A1.005":
            colect = 16

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD13A2.005":
            colect = 16

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD13A3.005":
            colect = 30

            startDtClt = datetime.datetime.strptime("2000-02-18", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD13A3.005":
            colect = 16

            startDtClt = datetime.datetime.strptime("2000-02-18", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD13C2.005":
            colect = 30

            startDtClt = datetime.datetime.strptime("2000-02-18", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD13Q1.005":
            colect = 16

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD14.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD14A1.005":
            colect = 1

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD14A2.005":
            colect = 8

            startDtClt = datetime.datetime.strptime("2000-02-24", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD15A2.005":
            colect = 8

            startDtClt = datetime.datetime.strptime("2000-02-18", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD17A2.005":
            colect = 8

            startDtClt = datetime.datetime.strptime("2000-02-18", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

        elif product.upper() == "MOD17A3.055":
            colect = 365

            startDtClt = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2010-12-31", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD44A.004":
            colect = 365

            startDtClt = datetime.datetime.strptime("2002-01-01", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2002-12-31", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD44B.005":
            colect = 365

            startDtClt = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2010-12-31", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD44B.051":
            colect = 365

            startDtClt = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")
            endDtClt = datetime.datetime.strptime("2013-12-31", "%Y-%m-%d")

            if self.startDate < startDtClt:
                self.startDate = startDtClt

            if self.endDate > endDtClt:
                self.endDate = endDtClt

        elif product.upper() == "MOD44W.005":
            colect = 365

        else:
            exit("-> Error: This satellite product was not supported")

        return colect
