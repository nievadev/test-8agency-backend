import dotenv

from flask import Flask, request

import config
from api import api


dotenv.load_dotenv()

app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)

app.register_blueprint(api, url_prefix='/api')