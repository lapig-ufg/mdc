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

    def __generateModis(self):
        self.exist = False
        self.layers = {}
        self.no_tiles = False

        aux = self.product.upper().split('.')
        product_name = aux[0]

        # try to get the version of product passed by params
        try:
            product_version = aux[1]
        except:
            product_version = None

        if product_name == "MOD09A1":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 8
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["sur_refl_b01"] = "-28672"
                self.layers["sur_refl_b02"] = "-28672"
                self.layers["sur_refl_b03"] = "-28672"
                self.layers["sur_refl_b04"] = "-28672"
                self.layers["sur_refl_b05"] = "-28672"
                self.layers["sur_refl_b06"] = "-28672"
                self.layers["sur_refl_b07"] = "-28672"
                self.layers["sur_refl_qc_500m"] = "4294967295"
                self.layers["sur_refl_szen"] = "0"
                self.layers["sur_refl_vzen"] = "0"
                self.layers["sur_refl_raz"] = "0"
                self.layers["sur_refl_state_500m"] = "65535"
                self.layers["sur_refl_day_of_year"] = "65535"

        elif product_name == "MOD09CMG":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 1
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.no_tiles = True

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
                self.layers["Coarse Resolution Brightness Temperature Band " \
                        + "20"] = "0"
                self.layers["Coarse Resolution Brightness Temperature Band " \
                        + "21"] = "0"
                self.layers["Coarse Resolution Brightness Temperature Band " \
                        + "31"] = "0"
                self.layers["Coarse Resolution Brightness Temperature Band " \
                        + "32"] = "0"
                self.layers["Coarse Resolution Granule Time"] = "0"
                self.layers["Coarse Resolution Band 3 Path Radiance"] = "-28672"
                self.layers["Coarse Resolution QA"] = "0"
                self.layers["Coarse Resolution Internal CM"] = "0"
                self.layers["Coarse Resolution State QA"] = "0"
                self.layers["N pixels averaged"] = "0"

        elif product_name == "MOD09GA":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 1
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["num_observations_1km"] = "-1"
                self.layers["state_1km_1"] = "65535"
                self.layers["SensorZenith_1"] = "-32767"
                self.layers["SensorAzimuth_1"] = "-32767"
                self.layers["Range_1"] = "65535"
                self.layers["SolarZenith_1"] = "-32767"
                self.layers["SolarAzimuth_1"] = "-32767"
                self.layers["gflags_1"] = "255"
                self.layers["orbit_pnt_1"] = "-1"
                self.layers["num_observations_500m"] = "-1"
                self.layers["sur_refl_b01_1"] = "-28672"
                self.layers["sur_refl_b02_2"] = "-28672"
                self.layers["sur_refl_b03_3"] = "-28672"
                self.layers["sur_refl_b04_4"] = "-28672"
                self.layers["sur_refl_b05_5"] = "-28672"
                self.layers["sur_refl_b06_6"] = "-28672"
                self.layers["sur_refl_b07_7"] = "-28672"
                self.layers["QC_500m_1"] = "787410671"
                self.layers["obscov_500m_1"] = "-1"
                self.layers["iobs_res_1"] = "255"
                self.layers["q_scan_1"] = "255"

        elif product_name == "MOD09GQ":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 1
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["num_observations"] = "-1"
                self.layers["sur_refl_b01_1"] = "-28672"
                self.layers["sur_refl_b02_1"] = "-28672"
                self.layers["QC_250m_1"] = "2995"
                self.layers["obscov_1"] = "-1"

        elif product_name == "MOD09Q1":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 8
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["sur_refl_b01"] = "-28672"
                self.layers["sur_refl_b02"] = "-28672"
                self.layers["sur_refl_qc_250m"] = "65535"

        elif product_name == "MOD11A1":
            self.temporalColect = 1

            if product_version == "004":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2007-01-03",
                        "%Y-%m-%d")

                self.layers["LST_Day_1km"] = "0"
                self.layers["QC_Day"] = "0"
                self.layers["Day_view_time"] = "0"
                self.layers["Day_view_angl"] = "255"
                self.layers["LST_Night_1km"] = "0"
                self.layers["QC_Night"] = "0"
                self.layers["Night_view_time"] = "0"
                self.layers["Night_view_angl"] = "255"
                self.layers["Emis_31"] = "0"
                self.layers["Emis_32"] = "0"
                self.layers["Clear_day_cov"] = "0"
                self.layers["Clear_night_cov"] = "0"

            elif product_version == "041":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["LST_Day_1km"] = "0"
                self.layers["QC_Day"] = "0"
                self.layers["Day_view_time"] = "0"
                self.layers["Day_view_angl"] = "255"
                self.layers["LST_Night_1km"] = "0"
                self.layers["QC_Night"] = "0"
                self.layers["Night_view_time"] = "0"
                self.layers["Night_view_angl"] = "255"
                self.layers["Emis_31"] = "0"
                self.layers["Emis_32"] = "0"
                self.layers["Clear_day_cov"] = "0"
                self.layers["Clear_night_cov"] = "0"

            elif product_version == "005":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["LST_Day_1km"] = "0"
                self.layers["QC_Day"] = None
                self.layers["Day_view_time"] = "0"
                self.layers["Day_view_angl"] = "255"
                self.layers["LST_Night_1km"] = "0"
                self.layers["QC_Night"] = None
                self.layers["Night_view_time"] = "0"
                self.layers["Night_view_angl"] = "255"
                self.layers["Emis_31"] = "0"
                self.layers["Emis_32"] = "0"
                self.layers["Clear_day_cov"] = "0"
                self.layers["Clear_night_cov"] = "0"

        elif product_name == "MOD11A2":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 8
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = None

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

        elif product_name == "MOD11B1":
            self.temporalColect = 1

            if product_version == "004":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2007-01-04",
                        "%Y-%m-%d")

                self.layers["LST_Day_5km"] = "0"
                self.layers["QC_Day"] = "0"
                self.layers["Day_view_time"] = "0"
                self.layers["Day_view_angl"] = "255"
                self.layers["LST_Night_5km"] = "0"
                self.layers["QC_Night"] = "0"
                self.layers["Night_view_time"] = "0"
                self.layers["Night_view_angl"] = "255"
                self.layers["Emis_20"] = "0"
                self.layers["Emis_22"] = "0"
                self.layers["Emis_23"] = "0"
                self.layers["Emis_29"] = "0"
                self.layers["Emis_31"] = "0"
                self.layers["Emis_32"] = "0"
                self.layers["LST_Day_5km_Aggregated_from_1km"] = "0"
                self.layers["LST_Night_5km_Aggregated_from_1km"] = "0"
                self.layers["QC_Emis"] = "0"

            elif product_version == "041":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["LST_Day_5km"] = "0"
                self.layers["QC_Day"] = "0"
                self.layers["Day_view_time"] = "0"
                self.layers["Day_view_angl"] = "255"
                self.layers["LST_Night_5km"] = "0"
                self.layers["QC_Night"] = "0"
                self.layers["Night_view_time"] = "0"
                self.layers["Night_view_angl"] = "255"
                self.layers["Emis_20"] = "0"
                self.layers["Emis_22"] = "0"
                self.layers["Emis_23"] = "0"
                self.layers["Emis_29"] = "0"
                self.layers["Emis_31"] = "0"
                self.layers["Emis_32"] = "0"
                self.layers["LST_Day_5km_Aggregated_from_1km"] = "0"
                self.layers["LST_Night_5km_Aggregated_from_1km"] = "0"
                self.layers["QC_Emis"] = "0"

            elif product_version == "005":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["LST_Day_5km"] = "0"
                self.layers["QC_Day"] = None
                self.layers["Day_view_time"] = "255"
                self.layers["Day_view_angl"] = "255"
                self.layers["LST_Night_5km"] = "0"
                self.layers["QC_Night"] = None
                self.layers["Night_view_time"] = "255"
                self.layers["Night_view_angl"] = "255"
                self.layers["Emis_20"] = "0"
                self.layers["Emis_22"] = "0"
                self.layers["Emis_23"] = "0"
                self.layers["Emis_29"] = "0"
                self.layers["Emis_31"] = "0"
                self.layers["Emis_32"] = "0"
                self.layers["LST_Day_5km_Aggregated_from_1km"] = "0"
                self.layers["LST_Night_5km_Aggregated_from_1km"] = "0"
                self.layers["QC_Emis"] = None
                self.layers["Percent_land_in_grid"] = "0"

        elif product_name == "MOD11C1":
            self.temporalColect = 1

            if product_version == "004":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2007-01-03",
                        "%Y-%m-%d")

                self.no_tiles = True

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

            elif product_version == "041":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.no_tiles = True

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

            elif product_version == "005":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.no_tiles = True

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

        elif product_name == "MOD11C2":
            self.temporalColect = 8
            self.no_tiles = True

            if product_version == "004":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2006-12-31",
                        "%Y-%m-%d")

                self.layers["Daytime land surface temperature"] = "0"
                self.layers["Daytime LSTE quality control"] = "0"
                self.layers["Daytime LST observation time (UTC)"] = "0"
                self.layers["Daytime LST view zenith angle"] = "255"
                self.layers["Days with clear-sky conditions and validated " \
                        + "LSTs"] = "0"
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

            elif product_version == "041":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["Daytime land surface temperature"] = "0"
                self.layers["Daytime LSTE quality control"] = "0"
                self.layers["Daytime LST observation time (UTC)"] = "0"
                self.layers["Daytime LST view zenith angle"] = "255"
                self.layers["Days with clear-sky conditions and validated " \
                        + "LSTs"] = "0"
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

            elif product_version == "005":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["Daytime land surface temperature"] = "0"
                self.layers["Daytime LSTE quality control"] = "0"
                self.layers["Daytime LST observation time (UTC)"] = "0"
                self.layers["Daytime LST view zenith angle"] = "255"
                self.layers["Days with clear-sky conditions and validated " \
                        + "LSTs"] = "0"
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

        elif product_name == "MOD11C3":
            self.temporalColect = 30
            self.no_tiles = True

            if product_version == "004":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2006-12-31",
                        "%Y-%m-%d")

                self.layers["Daytime land surface temperature"] = "0"
                self.layers["Daytime LSTE quality control"] = "0"
                self.layers["Daytime LST observation time (UTC)"] = "0"
                self.layers["Daytime LST view zenith angle"] = "255"
                self.layers["Days with clear-sky conditions and validated " \
                        + "LSTs"] = "0"
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

            elif product_version == "041":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["Daytime land surface temperature"] = "0"
                self.layers["Daytime LSTE quality control"] = "0"
                self.layers["Daytime LST observation time (UTC)"] = "0"
                self.layers["Daytime LST view zenith angle"] = "255"
                self.layers["Days with clear-sky conditions and validated " \
                        + "LSTs"] = "0"
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

            elif product_version == "005":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["Daytime land surface temperature"] = "0"
                self.layers["Daytime LSTE quality control"] = None
                self.layers["Daytime LST observation time (UTC)"] = "255"
                self.layers["Daytime LST view zenith angle"] = "255"
                self.layers["Days with clear-sky conditions and validated " \
                        + "LSTs"] = "0"
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

        elif product_name == "MOD11_L2":
            self.temporalColect = 1
            self.no_tiles = True

            if product_version == "004":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2007-01-03",
                        "%Y-%m-%d")

                self.layers["Land Surface Temperature"] = "0"
                self.layers["Daytime LSTE QC"] = "0"
                self.layers["LST Error"] = "0"
                self.layers["Band 31 Emissivity"] = "0"
                self.layers["Band 32 Emissivity"] = "0"
                self.layers["Zenith angle of the pixel view"] = "0"
                self.layers["LST Observation time"] = "0"
                self.layers["Latitude (every 5 scan lines/pixels"] = "-999"
                self.layers["Longitude (every 5 scan lines/pixels"] = "-999"

            elif product_version == "041":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2007-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["Land Surface Temperature"] = "0"
                self.layers["Daytime LSTE QC"] = "0"
                self.layers["LST Error"] = "0"
                self.layers["Band 31 Emissivity"] = "0"
                self.layers["Band 32 Emissivity"] = "0"
                self.layers["Zenith angle of the pixel view"] = "0"
                self.layers["LST Observation time"] = "0"
                self.layers["Latitude (every 5 scan lines/pixels"] = "-999"
                self.layers["Longitude (every 5 scan lines/pixels"] = "-999"

            elif product_version == "005":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["Land Surface Temperature"] = "0"
                self.layers["Daytime LSTE QC"] = None
                self.layers["LST Error"] = "0"
                self.layers["Band 31 Emissivity"] = "0"
                self.layers["Band 32 Emissivity"] = "0"
                self.layers["Zenith angle of the pixel view"] = "0"
                self.layers["LST Observation time"] = "0"
                self.layers["Latitude (every 5 scan lines/pixels"] = "-999"
                self.layers["Longitude (every 5 scan lines/pixels"] = "-999"

        elif product_name == "MOD13A1":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 16
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["500m_16_days_NDVI"] = "-3000"
                self.layers["500m_16_days_EVI"] = "-3000"
                self.layers["500m_16_days_VI_Quality"] = "65535"
                self.layers["500m_16_days_red_reflectance"] = "-1000"
                self.layers["500m_16_days_NIR_reflectance"] = "-1000"
                self.layers["500m_16_days_blue_reflectance"] = "-1000"
                self.layers["500m_16_days_MIR_reflectance"] = "-1000"
                self.layers["500m_16_days_view_zenith_angle"] = "-10000"
                self.layers["500m_16_days_sun_zenith_angle"] = "-10000"
                self.layers["500m_16_days_relative_azimuth_angle"] = "-4000"
                self.layers["500m_16_days_composite_day_of_the_year"] = "-1"
                self.layers["500m_16_days_pixel_reliability"] = "-1"

        elif product_name == "MOD13A2":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 16
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["1_km_16_days_NDVI"] = "-3000"
                self.layers["1_km_16_days_EVI"] = "-3000"
                self.layers["1_km_16_days_VI_Quality"] = "65535"
                self.layers["1_km_16_days_red_reflectance"] = "-1000"
                self.layers["1_km_16_days_NIR_reflectance"] = "-1000"
                self.layers["1_km_16_days_blue_reflectance"] = "-1000"
                self.layers["1_km_16_days_MIR_reflectance"] = "-1000"
                self.layers["1_km_16_days_view_zenith_angle"] = "-10000"
                self.layers["1_km_16_days_sun_zenith_angle"] = "-10000"
                self.layers["1_km_16_days_relative_azimuth_angle"] = "-4000"
                self.layers["1_km_16_days_composite_day_of_the_year"] = "-1"
                self.layers["1_km_16_days_pixel_reliability"] = "-1"

        elif product_name == "MOD13A3":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 30
                self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["1_km_monthly_NDVI"] = "-3000"
                self.layers["1_km_monthly_EVI"] = "-3000"
                self.layers["1_km_monthly_VI_Quality"] = "65535"
                self.layers["1_km_monthly_red_reflectance"] = "-1000"
                self.layers["1_km_monthly_NIR_reflectance"] = "-1000"
                self.layers["1_km_monthly_blue_reflectance"] = "-1000"
                self.layers["1_km_monthly_MIR_reflectance"] = "-1000"
                self.layers["1_km_monthly_view_zenith_angle"] = "-10000"
                self.layers["1_km_monthly_sun_zenith_angle"] = "-10000"
                self.layers["1_km_monthly_relative_azimuth_angle"] = "-4000"
                self.layers["1_km_monthly_pixel_raliability"] = "-1"

        elif product_name == "MOD13C1":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 16
                self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.no_tiles = True

                self.layers["CMG 0.05 Deg 16 days NDVI"] = "-3000"
                self.layers["CMG 0.05 Deg 16 days EVI"] = "-3000"
                self.layers["CMG 0.05 Deg 16 days VI Quality"] = "65535"
                self.layers["CMG 0.05 Deg 16 days red reflectance " \
                        + "(Band 1)"] = "-1000"
                self.layers["CMG 0.05 Deg 16 days NIR reflectance " \
                        + "(Band 2)"] = "-1000"
                self.layers["CMG 0.05 Deg 16 days blue reflectance " \
                        + "(Band 3)"] = "-1000"
                self.layers["CMG 0.05 Deg 16 days MIR reflectance " \
                        + "(Band 7)"] = "-1000"
                self.layers["CMG 0.05 Deg 16 days Avg sun zenith " \
                        + "angle"] = "-10000"
                self.layers["CMG 0.05 Deg 16 days NDVI std dev"] = "-3000"
                self.layers["CMG 0.05 Deg 16 days EVI std dev"] = "-3000"
                self.layers["CMG 0.05 Deg 16 days #1km pix used"] = "255"
                self.layers["CMG 0.05 Deg 16 days #1km pix +-30deg VZ"] = "255"
                self.layers["CMG 0.05 Deg 16 days pixel reliability"] = "-1"

        elif product_name == "MOD13C2.005":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 30
                self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                        "%Y-%m-%d")
                self.endDateProgram = None
                self.no_tiles = True

                self.layers["CMG 0.05 Deg Monthly NDVI"] = "-3000"
                self.layers["CMG 0.05 Deg Monthly EVI"] = "-3000"
                self.layers["CMG 0.05 Deg Monthly VI Quality"] = "65535"
                self.layers["CMG 0.05 Deg Monthly red reflectance " \
                        + "(Band 1)"] = "-1000"
                self.layers["CMG 0.05 Deg Monthly NIR reflectance " \
                        + "(Band 2)"] = "-1000"
                self.layers["CMG 0.05 Deg Monthly blue reflectance " \
                        + "(Band 3)"] = "-1000"
                self.layers["CMG 0.05 Deg Monthly MIR reflectance " \
                        + "(Band 7)"] = "-1000"
                self.layers["CMG 0.05 Deg Monthly Avg sun zenith " \
                        + "angle"] = "-1000"
                self.layers["CMG 0.05 Deg Monthly NDVI std dev"] = "-3000"
                self.layers["CMG 0.05 Deg Monthly EVI std dev"] = "-3000"
                self.layers["CMG 0.05 Deg Monthly #1km pix used"] = "255"
                self.layers["CMG 0.05 Deg Monthly #1km pix +-30deg VZ"] = "255"
                self.layers["CMG 0.05 Deg Monthly pixel reliability"] = "-1"

        elif product_name == "MOD13Q1.005":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 16
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["250m_16_days_NDVI"] = "-3000"
                self.layers["250m_16_days_EVI"] = "-3000"
                self.layers["250m_16_days_VI_Quality"] = "65535"
                self.layers["250m_16_days_red_reflectance"] = "-1000"
                self.layers["250m_16_days_NIR_reflectance"] = "-1000"
                self.layers["250m_16_days_blue_reflectance"] = "-1000"
                self.layers["250m_16_days_MIR_reflectance"] = "-1000"
                self.layers["250m_16_days_view_zenith_angle"] = "-10000"
                self.layers["250m_16_days_sun_zenith_angle"] = "-10000"
                self.layers["250m_16_days_relative_azimuth_angle"] = "-4000"
                self.layers["250m_16_days_composite_day_of_the_year"] = "-1"
                self.layers["250m_16_days_pixel_reliability"] = "-1"

        elif product_name == "MOD14":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 1
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.no_tiles = True

                self.layers["Fire mask"] = "0"
                self.layers["Algorithm QA"] = "294967295"
                self.layers["Fire Pixel Table"] = None

        elif product_name == "MOD14A1":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 1
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["Number_of_Days_01"] = "0"
                self.layers["Number_of_Days_02"] = None
                self.layers["Number_of_Days_03"] = "0"
                self.layers["Number_of_Days_04"] = None
                self.layers["Number_of_Days_05"] = None

        elif product_name == "MOD14A2":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 8
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["FireMask"] = "0"
                self.layers["QA"] = None

        elif product_name == "MOD15A2":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 8
                self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["Fpar_1km"] = "249-255"
                self.layers["Lai_1km"] = "249-255"
                self.layers["FparLai_QC"] = "255"
                self.layers["FparExtra_QC"] = "255"
                self.layers["FparStdDev_1k"] = "248-255"
                self.layers["LaiStdDev_1km"] = "248-255"

        elif product_name == "MOD17A2":
            self.temporalColect = 8

            if product_version == "005":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-02-18",
                        "%Y-%m-%d")
                self.endDateProgram = None

                self.layers["Gpp_1km"] = "32761-32767"
                self.layers["PsnNet_1km"] = "32761-32767"
                self.layers["Psn_QC_1km"] = "255"

            if product_version == "055":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2010-12-27",
                        "%Y-%m-%d")

                self.layers["Gpp_1km"] = "32761-32767"
                self.layers["PsnNet_1km"] = "32761-32767"
                self.layers["Psn_QC_1km"] = "255"

        elif product_name == "MOD17A3.055":
            if product_version == "055":
                self.exist = True
                self.temporalColect = 365
                self.initDateProgram = datetime.datetime.strptime("2000-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2010-12-31",
                        "%Y-%m-%d")

                self.layers["Gpp_1km"] = "0–65500"
                self.layers["Npp_1km"] = "65530–65535"
                self.layers["Gpp_Npp_QC_1km"] = "250-255"

        elif product_name == "MOD44A":
            if product_version == "004":
                self.exist = True
                self.temporalColect = 96
                self.initDateProgram = datetime.datetime.strptime("2002-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2002-10-16",
                        "%Y-%m-%d")

                self.layers["Metrics_01"] = "0"
                self.layers["Metrics_02"] = "255"
                self.layers["Metrics_03"] = "255"
                self.layers["Metrics_04"] = "0"

        elif product_name == "MOD44B":
            self.temporalColect = 365

            if product_version == "005":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-03-05",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2010-03-06",
                        "%Y-%m-%d")

                self.layers["Percent_Tree_Cover"] = "253"
                self.layers["Quality"] = None
                self.layers["Percent_Tree_Cover_SD"] = "-100"
                self.layers["Cloud"] = None

            elif product_version == "051":
                self.exist = True
                self.initDateProgram = datetime.datetime.strptime("2000-01-01",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2013-12-31",
                        "%Y-%m-%d")

                self.layers["Percent_Tree_Cover"] = "253"
                self.layers["Percent_NonTree_Vegetation"] = "253"
                self.layers["Percent_NonVegetated"] = "253"
                self.layers["Quality"] = None
                self.layers["Percent_Tree_Cover_SD"] = "-100"
                self.layers["Percent_NonVegetated_SD"] = "-100"
                self.layers["Cloud"] = None

        elif product_name == "MOD44W":
            if product_version == "005":
                self.exist = True
                self.temporalColect = 1
                self.initDateProgram = datetime.datetime.strptime("2000-02-24",
                        "%Y-%m-%d")
                self.endDateProgram = datetime.datetime.strptime("2000-02-25",
                        "%Y-%m-%d")

                self.layers["water_mask"] = "255"
                self.layers["water_mask_QA"] = "255"
        else:
            self.temporalColect = None
            self.initDateProgram = None
            self.endDateProgram = None
            self.nBand = None
            self.exist = False
