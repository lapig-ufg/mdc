import subprocess

TIF_CREATION_OPTIONS = ["COMPRESS=LZW", "INTERLEAVE=BAND", "TILED=YES", "BIGTIFF=IF_NEEDED"]
ABC_LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def calc(inputFiles, outputFile, expression, dataType, noData):
	
	command = ["gdal_calc.py"]
	
	for i in xrange(0,len(inputFiles)):
		inputFile = inputFiles[i]
		
		letter = "-" + ABC_LETTERS[i]
		expression = expression.replace("{"+str(i)+"}",ABC_LETTERS[i])

		command += [letter, inputFile]

	command += ['--NoDataValue=' + str(noData)]
	command += ["--type=" + dataType]
	command += ["--outfile=" + outputFile]
	command += ["--calc=" + '(' + expression + ')']
	__setCreationOption(command, '--co=', True)

	print(command)
	subprocess.call(command, stdout=subprocess.PIPE)
	print('finalizou')

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

def __setCreationOption(command, prefix, concat = False):
	for copt in TIF_CREATION_OPTIONS:
		if concat == True:
			command += [ str(prefix) + str(copt) ]
		else:
			command += [ prefix, copt ]