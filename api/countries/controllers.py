import pycountry
from flask import Blueprint, request, jsonify


countries = Blueprint('countries', __name__)


@countries.route('/')
def index() -> dict:

  countries = [{'name': country.name} for country in pycountry.countries]

  return jsonify(countries)