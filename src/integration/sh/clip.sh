#!/bin/bash

INPUT_SHP=$1
INPUT_RASTER=$2
OUTPUT_RASTER=$3
NODATA=$4
BB_TMP_RASTER=`basename $INPUT_RASTER .tif`_bbclip.tif

BASE=`basename $INPUT_SHP .shp`
EXTENT=`ogrinfo -so $INPUT_SHP $BASE | grep Extent \
| sed 's/Extent: //g' | sed 's/(//g' | sed 's/)//g' \
| sed 's/ - /, /g'`
EXTENT=`echo $EXTENT | awk -F ',' '{print $1 " " $4 " " $3 " " $2}'`
gdal_translate -ot Int16 -a_nodata $NODATA -co COMPRESS=LZW -co INTERLEAVE=BAND -co TILED=YES -co BIGTIFF=IF_NEEDED -projwin $EXTENT $INPUT_RASTER $BB_TMP_RASTER
gdalwarp -ot Int16 -srcnodata $NODATA -dstnodata $NODATA -co COMPRESS=LZW -co INTERLEAVE=BAND -co TILED=YES -co BIGTIFF=IF_NEEDED -r lanczos -cutline $INPUT_SHP $BB_TMP_RASTER $OUTPUT_RASTER
rm $BB_TMP_RASTER