import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# For the interactive map, we can use the folium library
import folium


# Load the data
df = pd.read_csv('data.csv')

# Create a GeoDataFrame
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Load the map of India from the shapefile
india = gpd.read_file('india.shp')

# Create a map centered around India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add the data points
for _, row in gdf.iterrows():
    folium.Marker([row['latitude'], row['longitude']]).add_to(m)

# Save the map as an HTML file
m.save('Output_InteractiveMap.html')
