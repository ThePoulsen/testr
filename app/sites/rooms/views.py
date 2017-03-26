## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for, jsonify
from app.services.services import errorMessage, successMessage
from app import app
from services import airbnb, airbnbSearch

roomsBP = Blueprint('roomsBP', __name__)

@roomsBP.route('/')
def roomsView():
    location = request.args.get('location')
    limit = request.args.get('limit')
    search=[]
    if location:
        if limit:
            search = airbnbSearch(location,limit)

    data = []
    for r in search:
        lat = r['listing']['lat']
        long = r['listing']['lng']
        price = r['pricing_quote']['localized_nightly_price']
        temp = {'lat':lat,
                'long':long,
                'price':price}
        data.append(temp)

    return render_template('sites/rooms/rooms.html', data=data)
