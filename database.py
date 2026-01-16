import os 
import mysql.connector
from mysql.connector import Error

def add_report(brand, model, date): 
    try: 
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"), 
            user=os.getenv("DB_USER"), 
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        print("Connection successful")

        print(f"Want to add: {brand}, {model}, {date}")
        cursor=conn.cursor()
        query=f"INSERT INTO stolen_reports VALUES ('{brand}', '{model}', '{date}')"
        cursor.execute(query)
        conn.commit()

        cursor.execute("SELECT * FROM stolen_reports")
        for row in cursor:
            print(row)

    except mysql.connector.Error as err: 
        print(f"Error: {err}")
    finally: 
        if 'cursor' in locals() and cursor: 
            cursor.close()
        if 'conn' in locals() and conn.is_connected(): 
            conn.close()
            print("Connection closed")


# Function that tallies num of theft for each car brand/model (what vehicle most vulnerable) and displayed to user 
