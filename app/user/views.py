## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

userBP = Blueprint('userBP', __name__)

@userBP.route('/profile')
def userProfileView():

    return render_template('user/profile.html')
