## -*- coding: utf-8 -*-

from api import gomoreAPI
import json
from flask import jsonify

class SijaxHandler(object):

    @staticmethod
    def listReturn(obj_response, values):
        data = {'limit':'50',
                'currency':values['currency']}

        if values['destCity'] == u'':
            obj_response.alert('You must specify a destination')

        else:

            if values['destCity'] != u'' or values['destCity'] != None:
                data['location'] = values['destCity']

                if values['checkin'] != u'':
                    data['checkin'] = values['checkin']

                if values['checkout'] != u'':
                    data['checkout'] = values['checkout']

                try:
                    req = gomoreAPI(data)
                    if not 'error' in req:
                        output = []
                        for r in req['hits']:
                            temp = {'ID':r['id'],
                                    'City':u'Århus',
                                    'geom':[r['lon'],r['lat']]}

                            if values['checkin'] != u'' and values['checkout'] != u'':
                                if r['pricing_quote']['available'] == True:
                                    output.append(temp)
                            else:
                                output.append(temp)

                        obj_response.call('clearMap')
                        obj_response.call('redrawMap', [output])

                    else:
                        obj_response.alert(req['error'])

                except Exception as E:
                    print E

    @staticmethod
    def ClearButton(obj_response):
        obj_response.call('clearMap')
