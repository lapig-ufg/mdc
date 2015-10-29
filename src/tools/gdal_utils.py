import subprocess

TIF_CREATION_OPTIONS = ["COMPRESS=LZW", "INTERLEAVE=BAND", "TILED=YES", "BIGTIFF=IF_NEEDED"]

def mosaic(inputFiles, outputFile, nodata = None):
	command = ["gdal_merge.py"]

	if nodata is not None:
		command += ["-n", str(nodata)]
		command += ["-a_nodata", str(nodata)]

	command += ["-o", outputFile]
	__setCreationOption(command, '-co')

	command += inputFiles

	subprocess.call(command, stdout=subprocess.PIPE)

def clip(imageFile, outputFile, shapeFile, nodata = None):
	command = ["gdalwarp", "-cutline", shapeFile]

	__setCreationOption(command, '-co')

	if nodata is not None:
		command += ["-srcnodata", str(nodata)]
		command += ["-dstnodata", str(nodata)]

	command += [imageFile, outputFile]

	subprocess.call(command, stdout=subprocess.PIPE)

def __setCreationOption(command, prefix):
	for copt in TIF_CREATION_OPTIONS:
		command += [ prefix, copt ]