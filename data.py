import pandas as pd 
import json


# Load csv file 
df = pd.read_csv(".cache/actes-criminels.csv")

# Keep only motor vehicule theft 
df = df[df['CATEGORIE'] == 'Vol de véhicule à moteur']

# Convert DATE to datetime 
df['DATE'] = pd.to_datetime(df['DATE'])

# Drop all rows without longiture and latitude 
df = df.dropna(subset=['X', 'Y', 'LONGITUDE', 'LATITUDE'])

#print(df)


def filter_data(year, month, time): 
    dataset = df 
    dataset = df[df['DATE'].dt.year == int(year)]
    #print(time)
    
    # Filter by month if not all month 
    if month != "all_months": 
        dataset = dataset[dataset['DATE'].dt.month == int(month)]
    
    # Filter by time of day if not all
    if time != "all": 
        dataset = dataset[dataset['QUART'] == time]
        
    print(len(dataset))
    return dataset

    
    






