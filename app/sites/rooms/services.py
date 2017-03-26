## -*- coding: utf-8 -*-
from flask import jsonify, json
import requests, os

def airbnb():

    data = [
      ('client_id', '3092nxybyb0otqw18e8nh5nty'),
      ('locale', 'en-US'),
      ('currency', 'USD'),
      ('grant_type','password'),
      ('username','henrik@vipilon.dk'),
      ('password',os.environ['p'])
    ]

    req = requests.post('https://api.airbnb.com/v1/authorize', data=data)

    return json.loads( req.text)

def airbnbSearch(location, limit):

    params = {'client_id': '3092nxybyb0otqw18e8nh5nty',
              'currency':'DKK',
              '_limit':str(limit),
              'location':location,
              'price_min':'100',
              'price_max':'350'}


    req = requests.get('https://api.airbnb.com/v2/search_results', params=params)

    return json.loads(req.text)['search_results']

