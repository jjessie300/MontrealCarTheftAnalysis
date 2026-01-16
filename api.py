import requests
import pandas as pd
import datetime
from geopy.geocoders import Nominatim 
from collections import Counter 


today = datetime.datetime.today()

interval = {
    "last_7_days": (today - datetime.timedelta(days=7)).strftime("%Y-%m-%d"), 
    "last_30_days": (today - datetime.timedelta(days=30)).strftime("%Y-%m-%d"), 
    "last_90_days": (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d")
}

url = "https://donnees.montreal.ca/api/3/action/datastore_search_sql"


# Number of incidents recently 
def incident_stats(): 
    stats = {} 

    for key, value in interval.items(): 
        sql_query = f"""
        SELECT * FROM "c6f482bf-bf0f-4960-8b2f-9982c211addd"
        WHERE "CATEGORIE" = 'Vol de véhicule à moteur'
        AND "DATE" >= '{value}'
        """

        response = requests.get(url, params={"sql": sql_query}).json()

        records = response['result']['records']
        # df = pd.DataFrame(records)
        #print(df)
        stats[key] = len(records)
 
    return stats

# incident_stats()



geolocator = Nominatim(user_agent="CarTheftDataAnalysis")

def vulnerable_borough(): 
    boroughs = {}
    sql_query = f"""
    SELECT * FROM "c6f482bf-bf0f-4960-8b2f-9982c211addd"
    WHERE "CATEGORIE" = 'Vol de véhicule à moteur'
    AND "DATE" >= '{interval['last_7_days']}'
    """
    response = requests.get(url, params={"sql": sql_query}).json()
    records = response['result']['records']
    df = pd.DataFrame(records)
    df = df.dropna(subset=['X', 'Y', 'LONGITUDE', 'LATITUDE'])

    areas = []

    for index, row in df.iterrows(): 
        coords = (row['LATITUDE'], row['LONGITUDE'])
        location = geolocator.reverse(coords)
        full_address = location.raw["address"]
        area = full_address.get("suburb") or full_address.get("town")
        if area:  
            areas.append(area)
        
        # print(areas)
    counts = Counter(areas).most_common(1)
    vulnerable_area, count = counts[0] 
    # print(vulnerable_area)
    return vulnerable_area
    
# vulnerable_borough()


def total_incidents_this_year(): 
    year = today.strftime("%Y")
    beg_year = year + "-01-01"
    sql_query = f"""
    SELECT * FROM "c6f482bf-bf0f-4960-8b2f-9982c211addd"
    WHERE "CATEGORIE" = 'Vol de véhicule à moteur'
    AND "DATE" >= '{beg_year}'
    """
    response = requests.get(url, params={"sql": sql_query}).json()
    records = response['result']['records']
    total_incidents = len(records) 
    return total_incidents


#def main(): 
    #print(vulnerable_borough())

#if __name__ == "__main__": 
    #main()