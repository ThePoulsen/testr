## -*- coding: utf-8 -*-

from app.sites.rooms.api import airbnbAPI
import json
from flask import jsonify

class SijaxHandler(object):

    @staticmethod
    def listReturn(obj_response, values):

        data = {'location':values['location'],
                'limit':'1',
                'currency':'DKK'}



        test = airbnbAPI(data)


        obj_response.script('$("#rooms").html(JSON.stringify('+test+', null, 4));')
