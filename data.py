import folium
from folium.plugins import MarkerCluster
import pandas as pd 
import json


# Load csv file 
df = pd.read_csv("actes-criminels.csv")

# Keep only motor vehicule theft 
df = df[df['CATEGORIE'] == 'Vol de véhicule à moteur']

# Convert DATE to datetime 
df['DATE'] = pd.to_datetime(df['DATE'])

# Drop all rows without longiture and latitude 
df = df.dropna(subset=['X', 'Y', 'LONGITUDE', 'LATITUDE'])

#print(df)

# Load geojson file
file_path = "/Users/jessi/Downloads/Montreal.geojson"

with open(file_path, 'r') as f: 
    geojson_data = json.load(f) 



def filter_data(year, month, time): 
    dataset = df 
    dataset = df[df['DATE'].dt.year == int(year)]
    #print(time)
    
    # Filter by month if not all month 
    if month != "all_months": 
        dataset[dataset['DATE'].dt.month == int(month)]
    
    # Filter by time of day if not all
    if time != "all": 
        dataset = dataset[dataset['QUART'] == time]
        
    return dataset


def generate_map(data, borough_outline): 
    m = folium.Map(location = [45.5500, -73.6667], zoom_start = 11)

    # Mark as Cluster
    cluster = MarkerCluster().add_to(m)

    print(data['DATE'])

    for index, row in data.iterrows():
        folium.Marker(
            location = [row["LATITUDE"], row["LONGITUDE"]], 
            popup = f"Date: {row['DATE']}"
        ).add_to(cluster)
    
    if borough_outline != None: 
        folium.GeoJson(geojson_data).add_to(m)
    
    m.save("static/map.html")


def intial_map(): 
    m = folium.Map(location = [45.5500, -73.6667], zoom_start = 11)
    m.save("static/map.html")
    
    






