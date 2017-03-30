# -*- coding: utf-8 -*-

import requests
import pprint
import json

def airbnbAPI(data):

    path = 'https://api.airbnb.com/v2/search_results'

    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}

    payload = {'client_id':'3092nxybyb0otqw18e8nh5nty',
               'location':data['location'],
               '_limit':data['limit'],
               'currency':data['currency'],
               'checkin':'2017-03-30',
               'checkout':'2017-03-31',
               'hosting_amenities':['15']}

    dataDict = {}

    req = requests.get(path, headers=headers, params=payload, data=json.dumps(dataDict, ensure_ascii=True)).text

    return req
