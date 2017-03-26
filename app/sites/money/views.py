## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

moneyBP = Blueprint('moneyBP', __name__)

@moneyBP.route('/')
def moneyView():
    return render_template('sites/money/money.html')
