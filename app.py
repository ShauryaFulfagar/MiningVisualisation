import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Load the data
df = pd.read_csv('data.csv')

# Create a GeoDataFrame
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Load the map of India from the shapefile
india = gpd.read_file('india.shp')

# Define a dictionary to map commodities to their real-life colors
color_map = {
    'Barite': '#B3B3B3',                # Light Gray
    'Alumina': '#F2F0A1',               # Pale Yellow
    'Aluminum': '#A9A9A9',              # Dark Gray
    'Bauxite': '#BC8F8F',               # Rosy Brown
    'Cement': '#D2B48C',                # Tan
    'Borax': '#E6E6E6',                 # Light Gray
    'Chromite': '#CD853F',              # Peru
    'Coal: bituminous': '#252525',      # Very Dark Gray
    'Copper': '#B87333',                # Copper
    'Copper: metal': '#B87333',         # Copper
    'Diamond': '#B9F2FF',               # Diamond Blue
    'Gold': '#FFCC66',                  # Gold
    'Ilmenite-rutile: ore': '#A1887F',  # Timberwolf
    'Iron and steel: crude steel': '#43464B',  # Charcoal
    'Kyanite': '#6A5ACD',               # Slate Blue
    'Lead: ore': '#525252',             # Dark Gray
    'Lead: primary': '#525252',         # Dark Gray
    'Lead: secondary': '#525252',       # Dark Gray
    'Lead-zinc: ore': '#525252',        # Dark Gray
    'Magnesite': '#CACACA',             # Silver
    'Manganese: ore': '#AA9D5A',        # Olive Green
    'Mica': '#A0522D',                  # Sienna
    'Petroleum: refined': '#800080',    # Purple
    'Phosphate rock': '#5DADE2',        # Sky Blue
    'Zinc': '#789048',                  # Moss Green
    'Coal: lignite': '#8B4513',         # Saddle Brown
}


# Plot the data on the static map
fig, ax = plt.subplots(figsize=(15, 10))  # Increase the size of the figure
plt.title("Map of Mineral and Metal Commodities in India")
india.plot(ax=ax, color='white', edgecolor='black')
for commodity, color in color_map.items():
    gdf[gdf['commodity'] == commodity].plot(
        ax=ax, markersize=20, color=color, marker='o', label=commodity)
# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Save the figure as an image file
plt.savefig('Output_MapOfCommodities.png')

# Count the number of mines for each commodity
commodity_counts = gdf['commodity'].value_counts()

# Create a new figure for the bar graph
plt.figure(figsize=(12.5, 11))

# Create a bar graph
bars = plt.barh(commodity_counts.index, commodity_counts.values, color=[
    color_map.get(commodity, '#333333') for commodity in commodity_counts.index])

# Add labels and title
plt.xlabel('Commodity')
plt.ylabel('Number of Mines')
plt.title('Number of Mines Across Different Commodities in India')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Save the figure as an image file
plt.savefig('Output_BarGraphOfCommodities.png')
