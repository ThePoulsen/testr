# -*- coding: utf-8 -*-

import requests
import json
from app.services.services import extendPoint, locationLatLng

def gomoreAPI(data):


    path = 'https://gomore.dk/api/javascript/v5/rental_ads/search'

    endpoint = ''

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

        nwLat = rng['nwLatLong'][0]
        nwLon = rng['nwLatLong'][1]
        seLat = rng['seLatLong'][0]
        seLon = rng['seLatLong'][1]

        dataDict = {}

        payload = {'country_id':1,
                   'limit':40,
                   'offset':0,
                   'tl_lat':nwLat,
                   'tl_lon':nwLon,
                   'br_lat':seLat,
                   'br_lon':seLon}

        req = requests.get(path, headers=headers, params=payload,
                           data=json.dumps(dataDict, ensure_ascii=True)).text

        req = json.loads(str(req))

        if req['status'] == 'success':
            if req['data'][u'count'] == 0:
                return {'error': 'No results'}
            else:
                return req['data']
        else:
            return {'error': 'No results'}
    else:
        return {'error':'Could not identify location'}
