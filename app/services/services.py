## -*- coding: utf-8 -*-
from flask import flash
from wtforms import widgets
import math, requests, json

def errorMessage(msg):
    return flash(str(msg), ('danger', 'Error'))

def successMessage(msg):
    return flash(str(msg), ('success','Success'))

# Select2 widget
class select2Widget(widgets.Select):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('data-role', u'select2')
        allow_blank = getattr(field, 'allow_blank', False)
        if allow_blank and not self.multiple:
            kwargs['data-allow-blank'] = u'1'

        return super(select2Widget, self).__call__(field, **kwargs)

# Select2 multiple widget
class select2MultipleWidget(widgets.Select):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('data-role', u'select2')
        allow_blank = getattr(field, 'allow_blank', False)
        if allow_blank and not self.multiple:
            kwargs['data-allow-blank'] = u'1'

        return super(select2MultipleWidget, self).__call__(field, multiple = True, **kwargs)

def extendPoint(lat, lng, distance):
    # Convert lat/lng to radians
    lat = math.radians(float(lat))
    lon = math.radians(float(lng))

    # Radius & Distance
    R = 6378000.0 #Radius of the Earth in meters
    d = distance

    # Bearings
    nwBearing = 5.49779 #Bearing is 315 degrees converted to radians.
    neBearing = 0.785398 #Bearing is 45 degrees converted to radians.
    seBearing = 2.35619 #Bearing is 135 degrees converted to radians.
    swBearing = 3.92699 #Bearing is 225 degrees converted to radians.

    nwLat = math.asin( math.sin(lat)*math.cos(d/R) + math.cos(lat)*math.sin(d/R)*math.cos(nwBearing))
    nwLon = lon + math.atan2(math.sin(nwBearing)*math.sin(d/R)*math.cos(lat), math.cos(d/R)-math.sin(lat)*math.sin(nwLat))

    neLat = math.asin( math.sin(lat)*math.cos(d/R) + math.cos(lat)*math.sin(d/R)*math.cos(neBearing))
    neLon = lon + math.atan2(math.sin(neBearing)*math.sin(d/R)*math.cos(lat), math.cos(d/R)-math.sin(lat)*math.sin(neLat))

    seLat = math.asin( math.sin(lat)*math.cos(d/R) + math.cos(lat)*math.sin(d/R)*math.cos(seBearing))
    seLon = lon + math.atan2(math.sin(seBearing)*math.sin(d/R)*math.cos(lat), math.cos(d/R)-math.sin(lat)*math.sin(seLat))

    swLat = math.asin( math.sin(lat)*math.cos(d/R) + math.cos(lat)*math.sin(d/R)*math.cos(swBearing))
    swLon = lon + math.atan2(math.sin(swBearing)*math.sin(d/R)*math.cos(lat), math.cos(d/R)-math.sin(lat)*math.sin(swLat))

    nwLat = math.degrees(nwLat)
    nwLon = math.degrees(nwLon)

    neLat = math.degrees(neLat)
    neLon = math.degrees(neLon)

    seLat = math.degrees(seLat)
    seLon = math.degrees(seLon)

    swLat = math.degrees(swLat)
    swLon = math.degrees(swLon)

    return {'nwLatLong':[nwLat,nwLon],
            'neLatLong':[neLat,neLon],
            'seLatLong':[seLat,seLon],
            'swLatLong':[swLat,swLon]}

def locationLatLng(location, language, country):
    path = 'http://api.geonames.org/searchJSON'

    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json'}

    payload = {'q':location,
               'lang':language,
               'country':country,
               'username': 'thepoulsen'}

    dataDict = {}

    req = requests.get(path, headers=headers, params=payload, data=json.dumps(dataDict, ensure_ascii=True)).text
    req = json.loads(req)

    if req['totalResultsCount'] == 0:
        return {'error':'No results found'}
    else:
        data = []
        for r in req['geonames']:
            temp = {'name':r['name'],
                    'lat':r['lat'],
                    'lng':r['lng']}
            data.append(temp)

        return {'success':data}
