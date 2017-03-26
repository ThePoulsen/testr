## -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import flask_sijax
from flask_htmlmin import HTMLMIN
from flask_security import Security, SQLAlchemyUserDatastore

# Setup Flask and read config from ConfigClass defined above
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Flask-SQLAlchemy
db = SQLAlchemy(app)

# Flask-mail
mail = Mail(app)

# HTML min
HTMLMIN(app)

# Flask-sijax
flask_sijax.Sijax(app)

# Import models
from app.user.models import User, Role

# Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

## import blueprints
from app.index.views import indexBP
from app.map.views import mapBP
from app.user.views import userBP
from app.sites.money.views import moneyBP
from app.sites.pets.views import petsBP
from app.sites.rooms.views import roomsBP
from app.sites.services.views import servicesBP
from app.sites.transport.views import transportBP
from app.sites.wifi.views import wifiBP

## Register blueprints
app.register_blueprint(indexBP, url_prefix='')
app.register_blueprint(mapBP, url_prefix='/map')
app.register_blueprint(userBP, url_prefix='/user')
app.register_blueprint(moneyBP, url_prefix='/money')
app.register_blueprint(petsBP, url_prefix='/pets')
app.register_blueprint(roomsBP, url_prefix='/rooms')
app.register_blueprint(servicesBP, url_prefix='/services')
app.register_blueprint(transportBP, url_prefix='/transport')
app.register_blueprint(wifiBP, url_prefix='/wifi')

# Error handlers

@app.errorhandler(404)
def page_not_found():
    return render_template('errors/404.html')

@app.route('/error404')
def error404():
    return render_template('errors/404.html')
