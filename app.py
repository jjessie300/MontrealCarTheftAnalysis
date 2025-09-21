from flask import Flask, render_template, url_for, request
import pandas as pd 
import json 
import folium 
from folium.plugins import MarkerCluster
import data, api

app = Flask(__name__)


@app.route('/')
def home(): 
    data.intial_map()
    incidents_this_year = int(api.total_incidents_this_year())
    print(incidents_this_year)
    return render_template('index.html', total=incidents_this_year)

@app.route('/filter_map', methods=['GET'])
def filter_map(): 
    year = request.args.get('year')
    month = request.args.get('month')
    time_of_day = request.args.get('day')
    show_borough = request.args.get('borough_outline')
    print(year)
    print(month)
    print(time_of_day)
    print(show_borough)
    data.generate_map(data.filter_data(year, month, time_of_day), show_borough)
    return render_template('index.html')

#@app.route('/recent_incidents')
#def show_recent(): 
    


if __name__ == "__main__": 
    app.run(debug=True)
