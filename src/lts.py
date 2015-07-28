#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
# (c) Copyright Marcelo Perini Veloso 2015
# ------------------------------------------
import sys
from region import Region

def print_args(argv):
	sys.exit("Usage: %s -d {Program Specification} -i {Index} -r {Region}\n" %
			argv[0] \
			+ "PROGRAM SPECIFICATION:\n" \
			+ "  A name of satellite observation program, ex:\n" \
			+ "    - Landsat\n    - Modis\n"\
			+ "INDEX:\n" \
			+ "  An expression to apply in images band's, ex:\n" \
			+ "    - \"B4-B3/B4+B3\"\n" \
			+ "REGION:\n" \
			+ "  Pass a name of specific region to clip in image, ex:\n" \
			+ "    - Brasil\n")

def main(argv):
	if len(argv) != 7:
		print_args(argv)
	elif argv[1] != "-d" or argv[3] != "-i" or argv[5] != "-r":
		print_args(argv)
	else:
		region = Region(argv[6])
		print region.tostring()

if __name__ == "__main__":
	main(sys.argv)
