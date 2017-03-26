## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

mapBP = Blueprint('mapBP', __name__)

@mapBP.route('/')
def mapView():
    return render_template('map/map.html')
