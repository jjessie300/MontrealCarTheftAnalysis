from flask import Flask, render_template, url_for, request
import pandas as pd 
import json 
import data

app = Flask(__name__)


@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/filter_map', methods=['GET'])
def filter_map(): 
    year = request.args.get('year')
    month = request.args.get('month')
    time_of_day = request.args.get('day')

    filtered = data.filter_data(year, month, time_of_day)

    print(year)
    print(month)
    print(time_of_day)

    return filtered[[
        "LATITUDE",
        "LONGITUDE",
        "DATE"
    ]].to_json(orient="records")



if __name__ == "__main__": 
    app.run(debug=True)
