from flask import Blueprint, request

from .countries.controllers import countries


api = Blueprint('api', __name__)

api.register_blueprint(countries, url_prefix='/countries')