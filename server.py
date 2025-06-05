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
    
    dashes = [145000000/4 * i for i in range(5)]
    mapped_dash = []
    min_dash = min(dashes)
    max_dash = max(dashes)
    if max_dash - min_dash == 0:
        mapped_dash = [0 for _ in dashes]
    else:
        mapped_dash = [int((val - min_dash) / (max_dash - min_dash) * 464) for val in dashes]
    mapped_dash.reverse()
    
    data_US = data['United States'] 
    
    mapped_data_US = []
    min_val = min(dashes)
    max_val = max(dashes)
    if max_val - min_val == 0:
        mapped_data_US = [0 for _ in data_US]
    else:
        mapped_data_US = [int((val - min_val) / (max_val - min_val) * 464) for val in data_US]
        
        
    data_N = data['Northeast Region'] 
    mapped_data_N = []
    min_val = min(dashes)
    max_val = max(dashes)
    if max_val - min_val == 0:
        mapped_data_N = [0 for _ in data_N]
    else:
        mapped_data_N = [int((val - min_val) / (max_val - min_val) * 464) for val in data_N]
        
    data_M = data['Midwest Region']
    mapped_data_M = []
    min_val = min(dashes)
    max_val = max(dashes)
    if max_val - min_val == 0:
        mapped_data_M = [0 for _ in data_M]
    else:
        mapped_data_M = [int((val - min_val) / (max_val - min_val) * 464) for val in data_M]
        
        
    data_W = data['West Region']
    mapped_data_W = []
    min_val = min(dashes)
    max_val = max(dashes)
    if max_val - min_val == 0:
        mapped_data_W = [0 for _ in data_W]
    else:
        mapped_data_W = [int((val - min_val) / (max_val - min_val) * 464) for val in data_W]
        
    data_S = data['South Region']
    mapped_data_S = []
    min_val = min(dashes)
    max_val = max(dashes)
    if max_val - min_val == 0:
        mapped_data_S = [0 for _ in data_S]
    else:
        mapped_data_S = [int((val - min_val) / (max_val - min_val) * 464) for val in data_S]
        
        
    return render_template('index.html', years=years, data=data, dashes=dashes, mapped_dash=mapped_dash, mapped_data_US=mapped_data_US,  mapped_data_N=mapped_data_N,  mapped_data_M=mapped_data_M,  mapped_data_W=mapped_data_W,  mapped_data_S=mapped_data_S)

@app.route('/year')
def year():
    year = request.args.get("year")
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    
    
    years = data['years']
    
    state_class_to_title = {
        "al": "Alabama",
        "ak": "Alaska", 
        "az": "Arizona",
        "ar": "Arkansas",
        "ca": "California",
        "co": "Colorado",
        "ct": "Connecticut",
        "de": "Delaware",
        "fl": "Florida",
        "ga": "Georgia",
        "hi": "Hawaii",
        "id": "Idaho",
        "il": "Illinois",
        "in": "Indiana",
        "ia": "Iowa",
        "ks": "Kansas",
        "ky": "Kentucky",
        "la": "Louisiana",
        "me": "Maine",
        "md": "Maryland",
        "ma": "Massachusetts",
        "mi": "Michigan",
        "mn": "Minnesota",
        "ms": "Mississippi",
        "mo": "Missouri",
        "mt": "Montana",
        "ne": "Nebraska",
        "nv": "Nevada",
        "nh": "New Hampshire",
        "nj": "New Jersey",
        "nm": "New Mexico",
        "ny": "New York",
        "nc": "North Carolina",
        "nd": "North Dakota",
        "oh": "Ohio",
        "ok": "Oklahoma",
        "or": "Oregon",
        "pa": "Pennsylvania",
        "ri": "Rhode Island",
        "sc": "South Carolina",
        "sd": "South Dakota",
        "tn": "Tennessee",
        "tx": "Texas",
        "ut": "Utah",
        "vt": "Vermont",
        "va": "Virginia",
        "wa": "Washington",
        "wv": "West Virginia",
        "wi": "Wisconsin",
        "wy": "Wyoming",
        "dc": "District of Columbia"
    }
    inv_map = {v: k for k, v in state_class_to_title.items()}
    data_labeled = {}
    
    vals = []
    
    for i in state_class_to_title.keys():
        data_labeled[i] = data[state_class_to_title[i]]
    
    for key in data_labeled:
        vals.append(data_labeled[key][years.index(int(year))])
        
    max_val = max(vals)
    min_val = min(vals)
    
    data_labeled = {k: v[years.index(int(year))] for k, v in data_labeled.items()}
    data_scaled = {k: int((v-min_val)/(max_val - min_val)*100) for k, v in data_labeled.items()}
    
    
    max_key = [key for key, val in data_labeled.items() if val == max_val][0]
    min_key = [key for key, val in data_labeled.items() if val == min_val][0]
    
    percent_max = round(max_val/data['United States'][years.index(int(year))],1)
    percent_max *= 100
    
    percent_min = round(min_val/data['United States'][years.index(int(year))],3)
    percent_min *= 100
    
    avg = sum(vals) / len(vals)
    
    return render_template('year.html', year=year, years=years, data_labeled=data_labeled, state_ids=list(state_class_to_title.keys()), max_val=max_val, min_val=min_val, data_scaled=data_scaled, max_key=state_class_to_title[max_key], min_key=state_class_to_title[min_key], avg=avg, max_percent=percent_max, min_percent=percent_min, us=data['United States'][years.index(int(year))])

@app.route('/about')
def about():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    years = data['years']
    return render_template('about.html', years=years)


app.run(debug=True)
