## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

servicesBP = Blueprint('servicesBP', __name__)

@servicesBP.route('/')
def servicesView():
    return render_template('sites/services/services.html')
