#!/bin/bash

MRT_HOME="$1"
HDF_FILE="$2"

RANDOM_DIR=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13)
RANDOM_TMP_DIR="/tmp/$RANDOM_DIR"

mkdir $RANDOM_TMP_DIR
cd $RANDOM_TMP_DIR
export MRT_HOME
MRT_DATA_DIR="$MRT_HOME/data"
export MRT_DATA_DIR
PATH="$MRT_HOME/bin:$PATH"
export PATH

HDR_FILE=$("$MRT_HOME/bin/resample" -h $HDF_FILE)

UL_CORNER_LATLON=$(cat "$HDR_FILE" | grep "UL_CORNER_LATLON" | cut -d\( -f2 | cut -d\) -f1 | xargs)
LR_CORNER_LATLON=$(cat "$HDR_FILE" | grep "LR_CORNER_LATLON" | cut -d\( -f2 | cut -d\) -f1 | xargs)

echo "$UL_CORNER_LATLON $LR_CORNER_LATLON"
cd ..
rm -R $RANDOM_TMP_DIR