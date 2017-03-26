## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

indexBP = Blueprint('indexBP', __name__)

# indexView
@indexBP.route('/')
def indexView():
    return render_template('index/index.html')
