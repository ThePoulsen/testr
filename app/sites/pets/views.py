## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

petsBP = Blueprint('petsBP', __name__)

@petsBP.route('/')
def petsView():
    return render_template('sites/pets/pets.html')
