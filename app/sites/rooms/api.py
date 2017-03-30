# -*- coding: utf-8 -*-

import requests
import pprint
import json

def airbnbAPI(data):

    path = 'https://api.airbnb.com/v2/search_results'

    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}

    payload = {'client_id':'3092nxybyb0otqw18e8nh5nty',
               'currency':data['currency']}

    if 'location' in data:
        payload['location'] = data['location']

    if 'checkin' in data and 'checkout' in data:
        payload['checkin'] = data['checkin']
        payload['checkout'] = data['checkout']

    dataDict = {}

    req = requests.get(path, headers=headers, params=payload, data=json.dumps(dataDict, ensure_ascii=True)).text

    return req

