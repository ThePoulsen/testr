## -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, SelectField, IntegerField, DateField, BooleanField
from wtforms.validators import InputRequired
from app.services.services import select2MultipleWidget, select2Widget

class searchForm(FlaskForm):
    destCity = StringField('Destination City')
    currency = SelectField('Currency', choices=[('DKK','DKK')])
    available = BooleanField('Show only available rooms')
    checkin = DateField('Check In', format="%Y-%m-%d")
    checkout = DateField('Check Out', format="%Y-%m-%d")
