import os 
import time
import pandas as pd 
import csv 

CACHE_EXPIRY = 24 * 60 * 60 # 24 hours 
CACHE_DIR = '.cache'
URL = (
    "https://donnees.montreal.ca/dataset/actes-criminels/"
    "resource/c6f482bf-bf0f-4960-8b2f-9982c211addd/"
    "download/actes-criminels.csv"
)
CACHE_FILENAME = "actes-criminels.csv"
CACHE_PATH = os.path.join(CACHE_DIR, CACHE_FILENAME)

def fetch_csv(): 
    # Check if cache directory exists 
    os.makedirs(CACHE_DIR, exist_ok=True)

    # Check if cached CSV exists
    if os.path.exists(CACHE_PATH): 
        # Calculate how old cached file is 
        age_file = time.time() - os.path.getmtime(CACHE_PATH)
        # Check if cached file expired 
        if age_file < CACHE_EXPIRY: 
            print("Using cached CSV")
            return 
    
    print("Downloading CSV and caching it")
    df = pd.read_csv(URL) # Load CSV 
    df.to_csv(CACHE_PATH, index=False, header=True, quoting=csv.QUOTE_NONNUMERIC) # Save CSV to cache 


def main(): 
    fetch_csv()

if __name__ == "__main__": 
    main()

