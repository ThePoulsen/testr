## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

roomsBP = Blueprint('roomsBP', __name__)

@roomsBP.route('/')
def roomsView():
    return render_template('sites/rooms/rooms.html')
