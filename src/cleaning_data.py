import os

import pandas as pd
import numpy as np
from pyproj import Proj, transform

'''
BICIMAD DATAFRAME CLEANING
'''

bicimad = pd.read_excel('../data/2018_Julio_Bases_Bicimad_EMT.xlsx')
bicimad.info()


'''There are two duplicates in ids which correspond to the 2 NANs in latitude. Drop these  rows'''
bicimad.id.value_counts()
bicimad[bicimad.name.str.contains('Segovia')]
bicimad.dropna(subset=['latitude'], inplace=True)

'''Joining coordinates into one single column'''
bicimad['COORDENADAS'] = bicimad[['longitude', 'latitude']].astype(str).apply(', '.join, axis=1)
bicimad.drop(['longitude', 'latitude'], axis=1, inplace=True)

'''Saving the cleaned DF'''
bicimad.to_csv('../data/bicimad_df_cleaned.csv', index=False)


'''
EMT DATAFRAME CLEANING
'''

emt = pd.read_csv('../data/Datos_abiertos__Elementos_de_la_Red_de_Autobuses_Urbanos_de_Madrid__EMT.csv',
                  sep=',')

'''NANs threshold'''
emt = emt.dropna(axis='columns', thresh= 2500)

'''Subset with the useful columns'''
subset = emt[['IDESTACION', 'DENOMINACION', 'X', 'Y', 'LINEAS']].copy()

'''Drop de null values in coordinates'''
subset.dropna(subset=['X'], inplace=True)

'''Drop duplicates in DENOMINACION'''
subset.drop_duplicates(subset=['DENOMINACION'], inplace=True)

'''Replace nans by 'not available information' in LINEAS column'''
subset.replace(np.nan, 'Not available information', inplace=True)

'''Convertir X e Y a long/lat'''
inProj = Proj(init='epsg:32230')
outProj = Proj(init='epsg:4326')

def convert_coordinates(long, lat):
    """
    Takes X, Y and transform them to our standard coordinates
        :param long: int
        :param lat: int
        :return: tuple with the transformed coordinates
    """
    long_converted, lat_converted = transform(inProj, outProj, long, lat)
    return long_converted, lat_converted


coordinates = list(map(lambda x, y: convert_coordinates(x, y), subset['X'], subset['Y']))
subset['X'] = list(map(lambda long: long[0], coordinates))
subset['Y'] = list(map(lambda lat: lat[1], coordinates))
subset['COORDENADAS'] = subset[['X', 'Y']].astype(str).apply(', '.join, axis=1)
subset.drop(['X', 'Y'], axis=1, inplace=True)

subset.to_csv('./data/emt_df_cleaned.csv', index=False)




