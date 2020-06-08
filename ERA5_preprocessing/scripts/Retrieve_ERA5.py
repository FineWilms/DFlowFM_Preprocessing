# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:43:47 2019

% area: N/W/S/E

@author: mcelman
"""

import cdsapi

c = cdsapi.Client()
year = '2018'
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type':'reanalysis',

        'variable': [
            '10m_u_component_of_wind',
            '10m_v_component_of_wind',
            'mean_sea_level_pressure',
            '2m_dewpoint_temperature',
            'relative_humidity',
            'surface_net_solar_radiation',
            '2m_temperature',
            'total_cloud_cover'
        ],
        'year':[
            year
        ],
        'area': '35.50/22.00/38.50/25.00',
        'month':['01' , '02', '03', '04' , '05', '06', '07', '08', '09', '10', '11', '12'],
        'day':[
            '01','02','03',
            '04','05','06',
            '07','08','09',
            '10','11','12',
            '13','14','15',
            '16','17','18',
            '19','20','21',
            '22','23','24',
            '25','26','27',
            '28','29','30',
            '31'
        ],
        'time':[
            '00:00','01:00','02:00',
            '03:00','04:00','05:00',
            '06:00','07:00','08:00',
            '09:00','10:00','11:00',
            '12:00','13:00','14:00',
            '15:00','16:00','17:00',
            '18:00','19:00','20:00',
            '21:00','22:00','23:00'
        ],
        'format':'netcdf'
    },
    'ERA5_%s.nc' %year)