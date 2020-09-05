#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To show geolocation data with basemap
"""

import pandas as pd
import matplotlib.pyplot as plt
#import mpl_toolkits
from mpl_toolkits.basemap import Basemap


# display world maps
m = Basemap(llcrnrlat = 10, urcrnrlat = 75, llcrnrlon = -180, urcrnrlon = -50, projection='merc')

airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
routes = pd.read_csv('routes.csv')

fig, ax = plt.subplots(figsize=(15,20))
plt.title("Scaled Up Earth With Coastlines")
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
m.scatter(x, y, s=1)
m.drawcoastlines()
plt.show()

# generate great circles from DFW to destinations
fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

geo_routes = pd.read_csv('geo_routes.csv')
geo_routes.info()
dfw = geo_routes.loc[geo_routes['source'] == "DFW"]

def create_great_circles(df):
    for index, row in df.iterrows():
        if abs(row['end_lat']-row['start_lat']) <180:
               if abs(row['end_lon']-row['start_lon']) <180:
                    (m.drawgreatcircle(row['start_lon'],row['start_lat'],
                                       row['end_lon'],row['end_lat']))



create_great_circles(dfw)
plt.show()