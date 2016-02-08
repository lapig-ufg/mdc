# Satellite Image Time-Series Tool

## Architecture
![alt tag](https://raw.githubusercontent.com/lapig-ufg/satellite-image-time-series/master/proj/img/architecture.png)

## Dependencies:
 - `python >= 2.7`
 - `redis-server >= 2.8.1`
 - `python-redis >= 2.10.3`
 - `mrt >= 4.1`
 - `pymodis >= 1.0`
 - `python-gdal >= 1.8`

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