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

        elif name == "MOD09CMG.005": # Não aceita tiles
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

        elif name == "MOD09GA.005":
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

        elif name == "MOD09GQ.005":
            self.layers["num_observations"] = "-1"
            self.layers["sur_refl_b01_1"] = "-28672"
            self.layers["sur_refl_b02_1"] = "-28672"
            self.layers["QC_250m_1"] = "2995"
            self.layers["obscov_1"] = "-1"

        elif name == "MOD09Q1.005":
            self.layers["sur_refl_b01"] = "-28672"
            self.layers["sur_refl_b02"] = "-28672"
            self.layers["sur_refl_qc_250m"] = "65535"

        elif name == "MOD11_L2.004" or name == "MOD11_L2.041": # não aceita tiles
            self.layers["Land Surface Temperature"] = "0"
            self.layers["Daytime LSTE QC"] = "0"
            self.layers["LST Error"] = "0"
            self.layers["Band 31 Emissivity"] = "0"
            self.layers["Band 32 Emissivity"] = "0"
            self.layers["Zenith angle of the pixel view"] = "0"
            self.layers["LST Observation time"] = "0"
            self.layers["Latitude (every 5 scan lines/pixels"] = "-999"
            self.layers["Longitude (every 5 scan lines/pixels"] = "-999"

        elif name == "MOD11_L2.005": # não aceita tiles
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

        elif name == "MOD11A1.005":
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

        elif name == "MOD11B1.005":
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

        elif name == "MOD11C1.004" or name == "MOD11C1.041": # não aceita tiles
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

        elif name == "MOD11C1.005": # não aceita tiles
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

        elif name == "MOD11C2.004" or name == "MOD11C2.041": # não aceita tiles
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

        elif name == "MOD11C2.005": # não aceita tiles
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

        elif name == "MOD11C3.004" or name == "MOD11C3.041": # não aceita tiles
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

        elif name ==" MOD11C3.005": # não aceita tiles
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

        elif name == "MOD13A1.005":
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

        elif name == "MOD13A2.005":
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

        elif name == "MOD13A3.005":
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

        elif name == "MOD13C1.005": # não aceita tiles
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
            self.layers["CMG 0.05 Deg 16 days Avg sun zenith angle"] = "-10000"
            self.layers["CMG 0.05 Deg 16 days NDVI std dev"] = "-3000"
            self.layers["CMG 0.05 Deg 16 days EVI std dev"] = "-3000"
            self.layers["CMG 0.05 Deg 16 days #1km pix used"] = "255"
            self.layers["CMG 0.05 Deg 16 days #1km pix +-30deg VZ"] = "255"
            self.layers["CMG 0.05 Deg 16 days pixel reliability"] = "-1"

        elif name == "MOD13C2.005": # não aceita tiles
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
            self.layers["CMG 0.05 Deg Monthly Avg sun zenith angle"] = "-1000"
            self.layers["CMG 0.05 Deg Monthly NDVI std dev"] = "-3000"
            self.layers["CMG 0.05 Deg Monthly EVI std dev"] = "-3000"
            self.layers["CMG 0.05 Deg Monthly #1km pix used"] = "255"
            self.layers["CMG 0.05 Deg Monthly #1km pix +-30deg VZ"] = "255"
            self.layers["CMG 0.05 Deg Monthly pixel reliability"] = "-1"

        elif name == "MOD13Q1.005":
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

        elif name == "MOD14.005": # problemas com os tiles
            self.layers["Fire mask"] = "0"
            self.layers["Algorithm QA"] = "294967295"
            self.layers["Fire Pixel Table"] = None

        elif name == "MOD14A1.005":
            self.layers["Number_of_Days_01"] = "0"
            self.layers["Number_of_Days_02"] = None
            self.layers["Number_of_Days_03"] = "0"
            self.layers["Number_of_Days_04"] = None
            self.layers["Number_of_Days_05"] = None

        elif name == "MOD14A2.005":
            self.layers["FireMask"] = "0"
            self.layers["QA"] = None

        elif name == "MOD15A2.005":
            self.layers["Fpar_1km"] = "249-255"
            self.layers["Lai_1km"] = "249-255"
            self.layers["FparLai_QC"] = "255"
            self.layers["FparExtra_QC"] = "255"
            self.layers["FparStdDev_1k"] = "248-255"
            self.layers["LaiStdDev_1km"] = "248-255"

        elif name == "MOD17A2.005" or name == "MOD17A2.055":
            self.layers["Gpp_1km: Gross Primary Production"] = "32761-32767"
            self.layers["PsnNet_1km: Net Photosynthesis (GPP – " \
                    + "maintenance respiration)"] = "32761-32767"
            self.layers["PSN_QC_1km: QC for GPP/PSN"] = "255"

        elif name == "MOD17A3.055":
            self.layers["Gridded 1 Km Annual Gross Primary " \
                    + "Productivity"] = "0–65500"
            self.layers["Gridded 1 Km Annual Net Primary " \
                    + "Productivity"] = "65530–65535"
            self.layers["Gpp_Npp_QC_1km"] = "250-255"

        elif name == "MOD44A.004":
            self.layers["Land Cover Change Metrics Past 1 Year"] = "0"
            self.layers["Labeled Land Cover Change Past 1 Year"] = "255"
            self.layers["Labeled Land Cover Change Past 1 Year QA"] = "255"
            self.layers["Algorithm Path Past 1 Year"] = "0"

        elif name == "MOD44B.005":
            self.layers["Percent Tree Cover"] = "253"
            self.layers["Quality"] = None
            self.layers["Percent Tree Cover SD"] = "-100"
            self.layers["Cloud"] = None

        elif name == "MOD44B.051":
            self.layers["Percent Tree Cover"] = "253"
            self.layers["Percent Non Tree Vegetation"] = "253"
            self.layers["Percent Non Vegetated"] = "253"
            self.layers["Quality"] = None
            self.layers["Percent Tree Cover SD"] = "-100"
            self.layers["Percent Non Vegetated SD"] = "-100"
            self.layers["Cloud"] = None

        elif name == "MOD44W.005":
            self.layers["Water Mask"] = "255"
            self.layers["Water Mask QA"] = "255"

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

        elif self.product.upper() == "MOD13A3.005":
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
