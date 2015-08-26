#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------
# Marcelo Perini Veloso
# <marcelo.perini.veloso@gmail.com>
#
# (c) Copyright Lapig UFG 2015
# http://www.lapig.iesa.ufg.br/
# ------------------------------------------
import datetime

class Modis:
    """ A class which define the modis product data """

    def __init__(self, product):
        self.product = product
        self.__generateModis()
        self.__createLayers(self.product.upper())

    def __createLayers(self, name):
        self.layers = {}

        if name == "MOD09A1.005":
            self.layers["500m Surface Reflectance Band 1 (620-670 nm)"] = \
                    "-28672"
            self.layers["500m Surface Reflectance Band 2 (841–876 nm)"] = \
                    "-28672"
            self.layers["500m Surface Reflectance Band 3 (459–479 nm)"] = \
                    "-28672"
            self.layers["500m Surface Reflectance Band 4 (545–565 nm)"] = \
                    "-28672"
            self.layers["500m Surface Reflectance Band 5 (1230–1250 nm)"] = \
                    "-28672"
            self.layers["500m Surface Reflectance Band 6 (1628–1652 nm)"] = \
                    "-28672"
            self.layers["500m Surface Reflectance Band 7 (2105–2155 nm)"] = \
                    "-28672"
            self.layers["500m Reflectance Band Quality"] = "4294967295"
            self.layers["Solar Zenith Angle"] = "0"
            self.layers["View Zenith Angle"] = "0"
            self.layers["Relative Azimuth Angle"] = "0"
            self.layers["500m State Flags"] = "65535"
            self.layers["Day of Year"] = "65535"

        elif name == "MOD09CMG.005":
            self.layers["Coarse Resolution Surface Reflectance Band 1 " \
                    + "(620–670 nm)"] = "-28672"
            self.layers["Coarse Resolution Surface Reflectance Band 2 " \
                    + "(841–876 nm)"] = "-28672"
            self.layers["Coarse Resolution Surface Reflectance Band 3 " \
                    + "(459–479 nm)"] = "-28672"
            self.layers["Coarse Resolution Surface Reflectance Band 4 " \
                    + "(545-565 nm)"] = "-28672"
            self.layers["Coarse Resolution Surface Reflectance Band 5 " \
                    + "(1230–1250 nm)"] = "-28672"
            self.layers["Coarse Resolution Surface Reflectance Band 6 " \
                    + "(1628–1652 nm)"] = "-28672"
            self.layers["Coarse Resolution Surface Reflectance Band 7 " \
                    + "(2105–2155 nm)"] = "-28672"
            self.layers["Coarse Resolution Solar Zenith Angle"] = "0"
            self.layers["Coarse Resolution View Zenith Angle"] = "0"
            self.layers["Coarse Resolution Relative Azimuth Angle"] = "0"
            self.layers["Coarse Resolution Ozone"] = "0"
            self.layers["Coarse Resolution Brightness Temperature Band 20"] = \
                    + "0"
            self.layers["Coarse Resolution Brightness Temperature Band 21"] = \
                    + "0"
            self.layers["Coarse Resolution Brightness Temperature Band 31"] = \
                    + "0"
            self.layers["Coarse Resolution Brightness Temperature Band 32"] = \
                    + "0"
            self.layers["Coarse Resolution Granule Time"] = "0"
            self.layers["Coarse Resolution Band 3 Path Radiance"] = "-28672"
            self.layers["Coarse Resolution QA"] = "0"
            self.layers["Coarse Resolution Internal CM"] = "0"
            self.layers["Coarse Resolution State QA"] = "0"
            self.layers["N pixels averaged"] = "0"

        elif name == "MOD09GA.005":
            self.layers["num_observations_1km"] = "-1"
            self.layers["State_1km"] = "65535"
            self.layers["SensorZenith"] = "-32767"
            self.layers["SensorAzimuth"] = "-32767"
            self.layers["Range"] = "65535"
            self.layers["SolarZenith"] = "-32767"
            self.layers["SolarAzimuth"] = "-32767"
            self.layers["gflags"] = "255"
            self.layers["orbit_pnt"] = "-1"
            self.layers["num_observations_500m"] = "-1"
            self.layers["sur_refl_b01"] = "-28672"
            self.layers["sur_refl_b02"] = "-28672"
            self.layers["sur_refl_b03"] = "-28672"
            self.layers["sur_refl_b04"] = "-28672"
            self.layers["sur_refl_b05"] = "-28672"
            self.layers["sur_refl_b06"] = "-28672"
            self.layers["sur_refl_b07"] = "-28672"
            self.layers["QC_500m"] = "787410671"
            self.layers["Obs_cov_500m"] = "-1"
            self.layers["iobs_res"] = "255"
            self.layers["q_scan"] = "255"

        elif name == "MOD09GQ.005":
            self.layers["num_observations"] = "-1"
            self.layers["250m Surface Reflectance Band 1 (620-670 nm)"] = \
                    + "-28672"
            self.layers["250m Surface Reflectance Band 2 (841-876 nm)"] = \
                    + "-28672"
            self.layers["250m Reflectance Band Quality"] = "2995"
            self.layers["obs_cov"] = "-1"

        elif name == "MOD09Q1.005":
            self.layers["250m Surface Reflectance Band 1 (620–670 nm)"] = \
                    + "-28672"
            self.layers["250m Surface Reflectance Band 2 (841–876 nm)"] = \
                    + "-28672"
            self.layers["250m Reflectance Band Quality"] = "65535"

        elif name == "MOD11_L2.004" or name == "MOD11_L2.041":
            self.layers["Land Surface Temperature"] = "0"
            self.layers["Daytime LSTE QC"] = "0"
            self.layers["LST Error"] = "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Zenith angle of the pixel view"] = "0"
            self.layers["LST Observation time"] = "0"
            self.layers["Latitude (every 5 scan lines/pixels"] = "-999"
            self.layers["Longitude (every 5 scan lines/pixels"] = "-999"

        elif name == "MOD11_L2.005":
            self.layers["Land Surface Temperature"] = "0"
            self.layers["Daytime LSTE QC"] = None
            self.layers["LST Error"] = "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Zenith angle of the pixel view"] = "0"
            self.layers["LST Observation time"] = "0"
            self.layers["Latitude (every 5 scan lines/pixels"] = "-999"
            self.layers["Longitude (every 5 scan lines/pixels"] = "-999"

        elif name == "MOD11A1.004" or name == "MOD11A1.041":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = "0"
            self.layers["Daytime LST observation time"] = "0"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = "0"
            self.layers["Nighttime LST observation time"] = "0"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Daytime clear-sky coverage"] = "0"
            self.layers["Nighttime clear-sky coverage"] = "0"

        elif name == "MOD11A1.005":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = None
            self.layers["Daytime LST observation time"] = "0"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = None
            self.layers["Nighttime LST observation time"] = "0"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Daytime clear-sky coverage"] = "0"
            self.layers["Nighttime clear-sky coverage"] = "0"

        elif name == "MOD11A2.005":
            self.layers["LST_Day_1km"] = "0"
            self.layers["QC_Day"] = "0" # See QA NOTE
            self.layers["Day_view_time"] = "255"
            self.layers["Day_view_angl"] = "255"
            self.layers["LST_Night_1km"] = "0"
            self.layers["QC_Night"] = "0" # See QA NOTE
            self.layers["Night_view_time"] = "255"
            self.layers["Night_view_angl"] = "255"
            self.layers["Emis_31"] = "0"
            self.layers["Emis_32"] = "0"
            self.layers["Clear_sky_days"] = "0"
            self.layers["Clear_sky_nights"] = "0"

        elif name == "MOD11B1.004" or name == "MOD11B1.041":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = "0"
            self.layers["Daytime LST observation time"] = "0"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = "0"
            self.layers["Nighttime LST observation time"] = "0"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Band 20 Emissivity"] = "0"
            self.layers["Band 22 Emissivity"] = "0"
            self.layers["Band 23 Emissivity"] = "0"
            self.layers["Band 29 Emissivity"] = "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Daytime 5-Km LST aggregated from 1-Km"] = "0"
            self.layers["Nighttime 5-Km LST aggregated from 1-Km"] = "0"
            self.layers["Quality control for retrieved emissivities"] = "0"

        elif name == "MOD11B1.005":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = None
            self.layers["Daytime LST observation time"] = "255"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = None
            self.layers["Nighttime LST observation time"] = "255"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Band 20 Emissivity"] = "0"
            self.layers["Band 22 Emissivity"] = "0"
            self.layers["Band 23 Emissivity"] = "0"
            self.layers["Band 29 Emissivity"] = "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Daytime 6-Km LST aggregated from 1-Km"] = "0"
            self.layers["Nighttime 5-Km LST aggregated from 1-Km"] = "0"
            self.layers["Quality control for retrieved emissivities"] = None
            self.layers["Land percentage in the grid"] = "0"

        elif name == "MOD11C1.004" or name == "MOD11C1.041":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = "0"
            self.layers["Daytime LST observation time (UTC)"] = "0"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = "0"
            self.layers["Nighttime LST observation time"] = "0"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Band 20 Emissivity"] = "0"
            self.layers["Band 22 Emissivity"] = "0"
            self.layers["Band 23 Emissivity"] = "0"
            self.layers["Band 29 Emissivity"] = "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Daytime 5-Km LST aggregated from 1-Km"] = "0"
            self.layers["Nighttime 5-Km LST aggregated from 1-Km"] = "0"
            self.layers["Quality control for retrieved emissivities"] = "0"

        elif name == "MOD11C1.005":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = None
            self.layers["Daytime LST observation time (UTC)"] = "255"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = None
            self.layers["Nighttime LST observation time (UTC)"] = "255"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Band 20 Emissivity"] = "0"
            self.layers["Band 22 Emissivity"] = "0"
            self.layers["Band 23 Emissivity"] = "0"
            self.layers["Band 29 Emissivity"] = "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Quality control for retrieved emissivities"] = None
            self.layers["Land percentage in the grid"] = "0"

        elif name == "MOD11C2.004" or name == "MOD11C2.041":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = "0"
            self.layers["Daytime LST observation time (UTC)"] = "0"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Days with clear-sky conditions and validated LSTs"] = \
                    + "0"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = "0"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Nights with clear-sky conditions and validated " \
                    + "LSTs"] = "0"
            self.layers["Band 20 Emissivity"] = "0"
            self.layers["Band 22 Emissivity"] = "0"
            self.layers["Band 23 Emissivity"] = "0"
            self.layers["Band 29 Emissivity"] = "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"

        elif name == "MOD11C2.005":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = "0"
            self.layers["Daytime LST observation time (UTC)"] = "0"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Days with clear-sky conditions and validated LSTs"] = \
                    + "0"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = "0"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Nights with clear-sky conditions and validated " \
                    + "LSTs"] = "0"
            self.layers["Band 20 Emissivity"] = "0"
            self.layers["Band 22 Emissivity"] = "0"
            self.layers["Band 23 Emissivity"] = "0"
            self.layers["Band 29 Emissivity"] = "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Land percentage in the grid"] = "0"

        elif name == "MOD11C3.004" or name == "MOD11C3.041":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = "0"
            self.layers["Daytime LST observation time (UTC)"] = "0"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Days with clear-sky conditions and validated LSTs"] = \
                    + "0"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = "0"
            self.layers["Nighttime LST observation time"] = "0"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Nights with clear-sky conditions and validated " \
                    + "LSTs"] = "0"
            self.layers["Band 20 Emissivity"] = "0"
            self.layers["Band 22 Emissivity"] = "0"
            self.layers["Band 23 Emissivity"] = "0"
            self.layers["Band 29 Emissivity"]= "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"

        elif name ==" MOD11C3.005":
            self.layers["Daytime land surface temperature"] = "0"
            self.layers["Daytime LSTE quality control"] = None
            self.layers["Daytime LST observation time (UTC)"] = "255"
            self.layers["Daytime LST view zenith angle"] = "255"
            self.layers["Days with clear-sky conditions and validated LSTs"] = \
                    + "0"
            self.layers["Nighttime land surface temperature"] = "0"
            self.layers["Nighttime LSTE quality control"] = None
            self.layers["Nighttime LST observation time (UTC)"] = "255"
            self.layers["Nighttime LST view zenith angle"] = "255"
            self.layers["Nights with clear-sky conditions and validated " \
                    + "LSTs"] = "0"
            self.layers["Band 20 Emissivity"] = "0"
            self.layers["Band 22 Emissivity"] = "0"
            self.layers["Band 23 Emissivity"] = "0"
            self.layers["Band 29 Emissivity"]= "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Quality control for retrieved emissivities"] = None
            self.layers["Land percentage in the grid"] = 0

        elif name == "MOD13A1.005":
            self.layers["500m 16 days NDVI"] = "-3000"
            self.layers["500m 16 days EVI"] = "-3000"
            self.layers["500m 16 days VI Quality detailed QA"] = "65535"
            self.layers["500m 16 days red reflectance (Band 1)"] = "-1000"
            self.layers["500m 16 days NIR reflectance (Band 2)"] = "-1000"
            self.layers["500m 16 days blue reflectance (Band 3)"] = "-1000"
            self.layers["500m 16 days MIR reflectance (Band 7)"] = "-1000"
            self.layers["500m 16 days view zenith angle"] = "-10000"
            self.layers["500m 16 days sun zenith angle"] = "-10000"
            self.layers["500m 16 days relative azimuth angle"] = "-4000"
            self.layers["500m 16 days composite day of the year"] = "-1"
            self.layers["500m 16 days pixel reliability summary QA"] = "-1"

        elif name == "MOD13A2.005":
            self.layers["1km 16 days NDVI"] = "-3000"
            self.layers["1km 16 days EVI"] = "-3000"
            self.layers["1km 16 days VI Quality detailed QA"] = "65535"
            self.layers["1km 16 days red reflectance (Band 1)"] = "-1000"
            self.layers["1km 16 days NIR reflectance (Band 2)"] = "-1000"
            self.layers["1km 16 days blue reflectance (Band 3)"] = "-1000"
            self.layers["1km 16 days MIR reflectance (Band 7)"] = "-1000"
            self.layers["1km 16 days view zenith angle"] = "-10000"
            self.layers["1km 16 days sun zenith angle"] = "-10000"
            self.layers["1km 16 days relative azimuth angle"] = "-4000"
            self.layers["1km 16 days composite day of the year"] = "-1"
            self.layers["1km 16 days pixel reliability summary QA"] = "-1"

        elif name == "MOD13A3":
            self.layers["1km monthly NDVI"] = "-3000"
            self.layers["1km monthly EVI"] = "-3000"
            self.layers["1km monthly VI Quality detailed QA"] = "65535"
            self.layers["1km monthly red reflectance (Band 1)"] = "-1000"
            self.layers["1km monthly NIR reflectance (Band 2)"] = "-1000"
            self.layers["1km monthly blue reflectance (Band 3)"] = "-1000"
            self.layers["1km monthly MIR reflectance (Band 7)"] = "-1000"
            self.layers["1km monthly view zenith angle"] = "-10000"
            self.layers["1km monthly sun zenith angle"] = "-10000"
            self.layers["1km monthly relative azimuth angle"] = "-4000"
            self.layers["1km monthly pixel reliability summary QA"] = "-1"

        elif name == "MOD13C1.005":
            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "65535" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-10000" })

            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "-1" })

        elif name == "MOD13C2.005":
            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "65535" })

            listlayers.append({ "fill" : "-1000" })

            listlayers.append({ "fill" : "-1000" })

            listlayers.append({ "fill" : "-1000" })

            listlayers.append({ "fill" : "-1000" })

            listlayers.append({ "fill" : "-10000" })

            listlayers.append({ "fill" : "-3000" })

            listlayers.append({ "fill" : "-3000" })

            listlayers.append({ "fill" : "255" })

            listlayers.append({ "fill" : "255" })

            listlayers.append({ "fill" : "-1" })

        elif name == "MOD13Q1.005":
            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "-3000" })

            listLayers.append({ "fill" : "65535" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-1000" })

            listLayers.append({ "fill" : "-10000" })

            listLayers.append({ "fill" : "-10000" })

            listLayers.append({ "fill" : "-4000" })

            listLayers.append({ "fill" : "-1" })

            listLayers.append({ "fill" : "-1" })

        elif name == "MOD14.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "294967295" })

            listLayers.append({ "fill" : None })

        elif name == "MOD14A1.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : None })

        elif name == "MOD14A2.005":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : None })

        elif name == "MOD15A2.005":
            listLayers.append({ "fill" : "249-255" })

            listLayers.append({ "fill" : "249-255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "248-255" })

            listLayers.append({ "fill" : "248-255" })

        elif name == "MOD17A2.005" or name == "MOD17A2.055":
            listLayers.append({ "fill" : "32761-32767" })

            listLayers.append({ "fill" : "32761-32767" })

            listLayers.append({ "fill" : "255" })

        elif name == "MOD17A3.055":
            listLayers.append({ "fill" : "0–65500" })

            listLayers.append({ "fill" : "65530–65535" })

            listLayers.append({ "fill" : "255-250" })

        elif name == "MOD44A.004":
            listLayers.append({ "fill" : "0" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "0" })

        elif name == "MOD44B.005":
            listLayers.append({ "fill" : "253" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "-100" })

            listLayers.append({ "fill" : None })

        elif name == "MOD44B.051":
            listLayers.append({ "fill" : "253" })

            listLayers.append({ "fill" : "253" })

            listLayers.append({ "fill" : "253" })

            listLayers.append({ "fill" : None })

            listLayers.append({ "fill" : "-100" })

            listLayers.append({ "fill" : "-100" })

            listLayers.append({ "fill" : None })

        elif name == "MOD44W.005":
            listLayers.append({ "fill" : "255" })

            listLayers.append({ "fill" : "255" })

    def __generateModis(self):
        self.exist = True

        if self.product.upper() == "MOD09A1.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD09CMG.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD09GA.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD09GQ.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD09Q1.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11A1.004":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2007-01-03",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD11A1.041":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11A1.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11A2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11B1.004":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2007-01-04",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD11B1.041":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11B1.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11C1.004":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2007-01-03",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD11C1.041":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11C1.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11C2.004":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2006-12-31",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD11C2.041":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11C2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11C3.004":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2006-12-31",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD11C3.041":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11C3.005":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11_L2.004":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2007-01-03",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD11_L2.041":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD11_L2.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD13A1.005":
            self.temporalColect = 16
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD13A2.005":
            self.temporalColect = 16
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD13A3":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD13C1.005":
            self.temporalColect = 16
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD13C2.005":
            self.temporalColect = 30
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD13Q1.005":
            self.temporalColect = 16
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD14.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD14A1.005":
            self.temporalColect = 1
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD14A2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD15A2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD17A2.005":
            self.temporalColect = 8
            self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                    "%Y-%m-%d")
            self.endDateProgram = None

        elif self.product.upper() == "MOD17A3.055":
            self.temporalColect = 365
            self.initDateProgram = datetime.datetime.strptime("2000-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2010-12-31",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD44A.004":
            self.temporalColect = 365
            self.initDateProgram = datetime.datetime.strptime("2002-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2002-12-31",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD44B.005":
            self.temporalColect = 365
            self.initDateProgram = datetime.datetime.strptime("2000-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2010-12-31",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD44B.051":
            self.temporalColect = 365
            self.initDateProgram = datetime.datetime.strptime("2000-01-01",
                    "%Y-%m-%d")
            self.endDateProgram = datetime.datetime.strptime("2013-12-31",
                    "%Y-%m-%d")

        elif self.product.upper() == "MOD44W.005":
            self.temporalColect = 365
            self.initDateProgram = None
            self.endDateProgram = None

        else:
            self.temporalColect = None
            self.initDateProgram = None
            self.endDateProgram = None
            self.nBand = None
            self.exist = False
