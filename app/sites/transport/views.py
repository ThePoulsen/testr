## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

transportBP = Blueprint('transportBP', __name__)

@transportBP.route('/')
def transportView():
    return render_template('sites/transport/transport.html')
