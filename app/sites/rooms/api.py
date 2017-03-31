# -*- coding: utf-8 -*-

import requests
import pprint
import json
from app.services.services import extendPoint, locationLatLng

def airbnbAPI(data):

    path = 'https://api.airbnb.com/v2/search_results'

    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}



    if 'location' in data:
        location = data['location']
    else:
        location = ''

    if 'language' in data:
        language = data['language']
    else:
        language = 'dk'

    if 'country' in data:
        country = data['country']
    else:
        country = 'dk'

    locData = locationLatLng(location, language, country)

    if 'success' in locData:
        coordinates = [locData['success'][0]['lat'],locData['success'][0]['lng']]

        # Coordinate range
        rng = extendPoint(lat=coordinates[0], lng=coordinates[1], distance=4500)

        ne_lat = rng['neLatLong'][0]
        ne_lon = rng['neLatLong'][1]
        sw_lat = rng['swLatLong'][0]
        sw_lon = rng['swLatLong'][1]

        payload = {'client_id':'3092nxybyb0otqw18e8nh5nty',
                   'currency':data['currency'],
                   'location':location,
                   '_limit':50,
                   'ne_lat':ne_lat,
                   'ne_lon':ne_lon,
                   'sw_lat':sw_lat,
                   'sw_lon':sw_lon,
                  }

        if 'checkin' in data and 'checkout' in data:
            payload['checkin'] = data['checkin']
            payload['checkout'] = data['checkout']

        dataDict = {}

        req = requests.get(path, headers=headers, params=payload, data=json.dumps(dataDict, ensure_ascii=True)).text

        req = json.loads(str(req))

        if req['status'] == 'success':
            return req
        else:
            return {'error': 'No results'}

    else:
        return {'error':'Could not identify location'}
