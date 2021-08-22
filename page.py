from flask import Flask

app = Flask(__name__)

import matplotlib.pyplot as plt, mpld3
import requests
import json
import numpy as np

def create_graph():
    ca = requests.get('https://api.covidtracking.com/v1/states/ca/current.json')
    ny = requests.get('https://api.covidtracking.com/v1/states/ny/current.json')
    ca_data = json.loads(ca.content.decode('utf-8'))
    ny_data = json.loads(ny.content.decode('utf-8'))

    np.random.seed(19680801)


    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    states = ('NY', 'CA')
    y_pos = np.arange(len(states))
    covid_cases = [ca_data['positive'], ny_data['positive']] 
    error = np.random.rand(len(states))

    ax.barh(y_pos, covid_cases, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(['NY', 'CA'])
    ax.set_xlabel('States')
    ax.set_title('Covid cases in the E.U.A')

    return mpld3.fig_to_html(fig)

@app.route("/")

def hello_world():
    return "<h1>New York and California covid cases currently</h1>"+create_graph()
