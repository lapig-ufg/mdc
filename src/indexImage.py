#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
from os import path

class indexImage:
    def __init__(self, formula, archives_list, start_date, end_date,
            default_path):
        self.formula = formula
        self.archives_list = archives_list
        self.start_date = start_date
        self.end_date = end_date

        self.default_path = default_path
        self.clip_path = path.join(self.default_path, "clip")
        self.target_path = path.join(self.default_path, "index")
