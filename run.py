import dotenv
from flask import Flask, request
from flask.helpers import make_response
from flask.wrappers import Response

import config
from api import api


dotenv.load_dotenv()

app = Flask(__name__)

app.config.from_object(config.Config)


@app.after_request
def cors(response: Response) -> Response:
  if request.headers['Origin'] in app.config['WHITE_HOST']:
    response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

    if request.method == 'OPTIONS':
      return make_response(response, 200)

  return response


app.register_blueprint(api, url_prefix='/api')