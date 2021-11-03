import dotenv
from flask import Flask, request
from flask.wrappers import Response

import config
from api import api


dotenv.load_dotenv()

app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)


@app.after_request
def cors(response: Response) -> Response:
  if request.headers['Origin'] in app.config['WHITE_HOST']:
    response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']

  return response


app.register_blueprint(api, url_prefix='/api')