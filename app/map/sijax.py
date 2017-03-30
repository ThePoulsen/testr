## -*- coding: utf-8 -*-

from app.sites.rooms.api import airbnbAPI
import json
from flask import jsonify

class SijaxHandler(object):

    @staticmethod
    def listReturn(obj_response, values):
        data = {'limit':'50',
                'currency':values['currency']}

        if values['destCity'] != u'' or values['destCity'] != None:
            data['location'] = values['destCity']

        if values['checkin'] != u'':
            data['checkin'] = values['checkin']

        if values['checkout'] != u'':
            data['checkout'] = values['checkout']

        try:
            req = json.loads(airbnbAPI(data))['search_results']
            output = []

            for r in req:
                temp = {'ID':r['listing']['id'],
                        'City':r['listing']['city'],
                        'geom':[r['listing']['lng'],r['listing']['lat']]}

                if values['checkin'] != u'' and values['checkout'] != u'':
                    if r['pricing_quote']['available'] == True:
                        output.append(temp)
                else:
                    output.append(temp)

            obj_response.call('clearMap')
            obj_response.call('redrawMap', [output])

        except Exception as E:
            print E

    @staticmethod
    def ClearButton(obj_response):
        obj_response.call('clearMap')
