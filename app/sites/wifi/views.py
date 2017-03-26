## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

wifiBP = Blueprint('wifiBP', __name__)

@wifiBP.route('/')
def wifiView():
    return render_template('sites/wifi/wifi.html')
