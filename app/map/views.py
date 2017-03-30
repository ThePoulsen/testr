## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for, g, jsonify
from app.services.services import errorMessage, successMessage
from app import app
from sijax import SijaxHandler
import flask_sijax
from forms import searchForm

mapBP = Blueprint('mapBP', __name__)

@flask_sijax.route(mapBP, '/', methods=['GET'])
def mapView():

    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()

    form = searchForm(currency='DKK')

    return render_template('map/map.html', form=form)
