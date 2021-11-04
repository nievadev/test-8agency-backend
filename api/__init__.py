from flask import Blueprint

from .countries.controllers import countries
from .attendees.controllers import attendees


api = Blueprint('api', __name__)

api.register_blueprint(countries, url_prefix='/countries')
api.register_blueprint(attendees, url_prefix='/attendees')