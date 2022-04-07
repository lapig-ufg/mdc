# MODIS Data Cube

This software organize 
This software is responsible for downloading and processing various MODIS products. (see [modis.json](https://github.com/lapig-ufg/mdc/blob/master/src/conf/modis.json)). See the final results:
 - [MOD13Q1 - NDVI](https://maps.lapig.iesa.ufg.br/?layers=pa_br_ndvi_250_lapig)
 - [MOD11B1 - LSTM](https://maps.lapig.iesa.ufg.br/?layers=pa_br_lst_day_250_lapig)

## Architecture
![alt tag](https://raw.githubusercontent.com/lapig-ufg/satellite-image-time-series/master/proj/img/architecture-modis.png)

## Prequisites

- `Docker >= 19.03`
- `Docker-Compose >= 1.25.0`
- `Git >= 2.25`

## Dependencies:
 - `python >= 2.7`
 - `redis-server >= 2.8.1`
 - `redis == 3.5.3`
 - `mrt >= 4.1`
 - `pymodis >= 1.0`
 - `GDAL == 2.4.0`

## Running:
 1. Start Redis-server
 ```
 redis-server
 ```
 2. Start Sitsd
 ```
 python sitsd.py
 ```
 3. Send a processing 
 ```
 python sits.py -d modis -p MOD13Q1.006 -r brasil -s 2014-01-01 -e 2016-01-01
 ```
