from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm

from expmarket import *

# import yfinance as yf

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/mlanal/<name>')
def success(name):
   if(request.method == 'GET'):
      data = {
         "Modules" : 15,
         "Subject" : name,
      }
  
      return jsonify(data)

@app.route('/anal/<name>')
def successnew(name):
   if(request.method == 'GET'):
      data = {
         "Modules" : 15,
         "Subject" : name,
      }
  
      return jsonify(data)

if __name__ == '__main__':    
   app.run(debug=True)

