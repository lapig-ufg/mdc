#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import Queue
import string
import subprocess
from os import path
from modis import Modis
from common import createPath

class indexImage:
    def __init__(self, formula, program, product, startDate, endDate, region,
            archives_list, default_path):
        self.formula = formula
        self.program = program
        self.product = product
        self.startDate = startDate
        self.endDate = endDate
        self.region = region
        self.archives_list = archives_list

        self.elements_dict = {}
        self.createQueueLetters()
        self.createFormula()

        self.default_path = default_path
        self.clip_path = path.join(self.default_path, "clip")
        self.target_path = path.join(self.default_path, "index")

    def createQueueLetters():
        self.queue_letters = Queue.Queue()

        for letter in string.uppercase[:26]:
            self.queue_letters.put(letter)

    def createFormula():
        if self.program == "Modis":
            product = Modis(self.product)
#        else:
#            product = Landsat(self.product)

        if product.exist:
            for band in product.layers:
                if ('{' + band + '}') in self.formula:
                    if not self.queue_letters.empty():
                        letter = self.queue_letters.get()

                        self.formula = self.formula.replace('{' + band + '}',
                                letter)

                        self.elements_dict[band] = letter

        else:
            exit("[INDEX MODULE    ] |-> Error: %s product does not "
                    % self.product + "supported")

    def run():
        if self.formula and self.program and self.product \
                and self.archives_list and self.start_date and self.end_date \
                and self.default_path and self.clip_path and self.target_path:
            if not createPath(self.target_path):
                exit("[INDEX MODULE     ] |-> Error: Directory %s does "
                        % self.target_path + "not exist.")

            if not createPath(self.clip_path):
                exit("[INDEX MODULE     ] |-> Error: Directory %s does "
                        % self.clip_path + "not exist.")

            if self.program.upper() == "MODIS":
                program = Modis(self.product)

            if program.exist:

                args = ["gdal_calc.py"]

                for band in self.elements_dict:
                    args += ['-' + self.elements_dict[band],
                            self.archives_list[band]]

                out_file = self.program + '_' + self.product \
                    + '_' + self.startDate + '_' \
                    + self.endDate + '_' \
                    + self.region + '_' + self.formula + ".tif"

                args += ["--outfile=" + self.target_path + out_file]
                args += ['--calc="' + self.formula + '"']

                try:
                    subprocess.call(args, stdout=subprocess.PIPE)
                    print("[INDEX MODULE     ]   |-> Finish index " \
                            + "of %s" % out_file)
                except:
                    print("[INDEX MODULE     ]   |-> Error: was " \
                            + "not possible to clip %s" % out_file)

            else:
                print("[INDEX MODULE     ] |-> Error: %s product does not "
                        % self.product + "supported")
                return False

        else:
            return False
