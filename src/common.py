#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------

def printUsage(usage):
    exit(usage)

def mapDict(args, usage):
    """ This function get the arguments by parameters and put all
      " system arguments in a dict variable considering the description
      " of usage
      """
    argd = { }

    for i in range(len(args)):
        if args[i] == "-d": # program specification
            try:
                argd["-d"] = args[i + 1]
            except:
                printUsage(usage)
        elif args[i] == "-p": # product
            try:
                argd["-p"] = args[i + 1]
            except:
                printUsage(usage)
        elif args[i] == "-r": # region
            try:
                argd["-r"] = args[i + 1]
            except:
                printUsage(usage)
        elif args[i] == "-s": # start date
            try:
                argd["-s"] = args[i + 1]
            except:
                printUsage(usage)
        elif args[i] == "-e": # end date
            try:
                argd["-e"] = args[i + 1]
            except:
                printUsage(usage)
        elif args[i] == "-t": # target path
            try:
                argd["-t"] = args[i + 1]
            except:
                printUsage(usage)

    return argd
