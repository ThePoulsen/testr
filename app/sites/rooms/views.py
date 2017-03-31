## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for, g
from app.services.services import errorMessage, successMessage
from app import app
import flask_sijax
from sijax import SijaxHandler
from forms import searchRoomForm

roomsBP = Blueprint('roomsBP', __name__)

@flask_sijax.route(roomsBP, '/', methods=['GET'])
def roomMapSearchView():

    kwargs = {'title':'Search for rooms'}

    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()

    form = searchRoomForm(currency='DKK')

    return render_template('sites/rooms/rooms.html', form=form, **kwargs)
