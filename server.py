from flask import Flask
from flask import render_template, request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    years = data['years']
    return render_template('index.html', years=years)

@app.route('/year')
def year():
    year = request.args.get("year")
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    years = data['years']
    return render_template('year.html', year=year, years=years)

@app.route('/about')
def about():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    years = data['years']
    return render_template('about.html', years=years)

app.run(debug=True)
