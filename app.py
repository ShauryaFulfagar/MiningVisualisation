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
    'Barite': '#777A86',
    'Alumina': '#C0C085',
    'Aluminum': '#7E7E80',
    'Bauxite': '#AD6F69',
    'Cement': '#8C7853',
    'Borax': '#9AB973',
    'Chromite': '#D9A441',
    'Coal: bituminous': '#2C2B2B',
    'Copper': '#B87333',
    'Copper: metal': '#B87333',  # Adding the new commodity
    'Diamond': '#B9F2FF',
    'Gold': '#FFCC66',
    'Ilmenite-rutile: ore': '#C3B091',
    'Iron and steel: crude steel': '#43464B',
    'Kyanite': '#6A5ACD',
    'Lead: ore': '#8D4E85',
    'Lead: primary': '#8D4E85',
    'Lead: secondary': '#8D4E85',
    'Lead-zinc: ore': '#8D4E85',
    'Magnesite': '#CABBAC',
    'Manganese: ore': '#AF9B60',
    'Mica': '#BA9F93',
    'Petroleum: refined': '#4B0082',
    'Phosphate rock': '#2E86C1',
    'Zinc': '#7C886A',
    'Coal: lignite': '#964B00',
    # Add more commodities and their colors here
}


# Plot the data on the static map
fig, ax = plt.subplots(figsize=(10, 10))  # Increase the size of the figure
plt.title("Map of Mineral and Metal Commodities in India")
india.plot(ax=ax, color='white', edgecolor='black')
for commodity, color in color_map.items():
    gdf[gdf['commodity'] == commodity].plot(ax=ax, markersize=20, color=color, marker='o', label=commodity)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Move the legend outside the plot

# Save the figure as an image file
plt.savefig('Output_MapOfCommodities.png')

# Count the number of mines for each commodity
commodity_counts = gdf['commodity'].value_counts()

# Create a new figure for the bar graph
plt.figure(figsize=(10, 10))

# Create a bar graph
bars = plt.bar(commodity_counts.index, commodity_counts.values, color=[color_map.get(commodity, '#333333') for commodity in commodity_counts.index])

# Add labels and title
plt.xlabel('Commodity')
plt.ylabel('Number of Mines')
plt.title('Number of Mines Across Different Commodities in India')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Save the figure as an image file
plt.savefig('Output_BarGraphOfCommodities.png')

# Show the plot
plt.show()