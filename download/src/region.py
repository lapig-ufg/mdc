#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
# (c) Copyright Marcelo Perini Veloso 2015
# ------------------------------------------

class Region:
    def __init__(self, name):
        self.name = name
        self.ids = self.__selectIds(name)

    def tostring(self):
        return "Region name: '" + self.name + "', ids: " + str(self.ids)

    def printIds(self):
        str = ""
        for i in range(len(self.ids) - 1):
            str += self.ids[i] + ','

        str += self.ids[-1]
        return str


    def __selectIds(self, name):
        if name.upper() == "BRASIL" or name.upper() == "BRAZIL":
            return ["h13v11", "h12v08", "h14v09", "h14v10", "h13v12",
                    "h10v08", "h10v09", "h11v08", "h11v09", "h11v10", "h12v11",
                    "h13v08", "h12v09", "h12v10", "h14v11", "h13v09", "h13v10"]
        else:
            return []
