## -*- coding: utf-8 -*-

from flask import render_template, Blueprint, request, url_for
from app.services.services import errorMessage, successMessage
from app import app

apiBP = Blueprint('apiBP', __name__)
