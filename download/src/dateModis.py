#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
# (c) Copyright Marcelo Perini Veloso 2015
# ------------------------------------------
import datetime
from sys import exit

class DateModis:
    def __init__(self, product, startDate, endDate):
        self.product = product
        self.startDate = startDate
        self.endDate = endDate
        self.datesList = self.__makeDate(product, startDate, endDate)

    def __makeDate(self, product, startDate, endDate):
        try:
            startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
            endDate = datetime.datetime.strptime(endDate, "%Y-%m-%d")
        except:
            exit("-> Error: Bad date format in " + startDate + " and "
                    + endDate)

        dateList = []
        if product.upper() == "MOD11A1.005":
            colect = 15
        else:
            exit("-> Error: This program was not defined")

        start = startDate
        end = start

        while end < endDate:
            end = start + datetime.timedelta(days=colect)

            if end > endDate:
                end = endDate

            dateList.append({"start" : start.strftime("%Y-%m-%d"),
                "end" : end.strftime("%Y-%m-%d")})

            start = end + datetime.timedelta(days=1)

        return dateList
