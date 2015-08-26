#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------

from sys import exit
from os import path
from os import makedirs

def createDefaultPath():
    """ Function which create a string of $HOME/Maps path """

    # default work directory
    home_path = path.expanduser("~")
    default_path = path.join(home_path, "Maps")
    return default_path

def createPath(tpath):
    """ This method try to create the path passed by parameter if
        " not exist
        """

    if not path.exists(tpath):
        try:
            makedirs(tpath)
        except:
            exit(" |-> Error: Directory %s does " % tpath \
                    + "not exist and it is impossible to create")

def mapDict(argv, msg):
    """ This function get the arguments by parameters and put all
      " system arguments in a dict variable considering the description
      " of usage
      """
    argd = { }

    for i in range(len(argv)):
        if argv[i] == "-d": # program specification
            try:
                argd["-d"] = argv[i + 1]
            except:
                exit(msg)
        elif argv[i] == "-p": # product
            try:
                argd["-p"] = argv[i + 1]
            except:
                exit(msg)
        elif argv[i] == "-r": # region
            try:
                argd["-r"] = argv[i + 1]
            except:
                exit(msg)
        elif argv[i] == "-s": # start date
            try:
                argd["-s"] = argv[i + 1]
            except:
                exit(msg)
        elif argv[i] == "-e": # end date
            try:
                argd["-e"] = argv[i + 1]
            except:
                exit(msg)
        elif argv[i] == "-i": # index
            try:
                argd["-i"] = argv[i + 1]
            except:
                exit(msg)
        elif argv[i] == "-t": # target path
            try:
                argd["-t"] = argv[i + 1]
            except:
                exit(msg)

    return argd
