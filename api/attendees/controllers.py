from typing import Optional

from flask import Blueprint, request


attendees = Blueprint('attendees', __name__)


def index_get() -> bytes:
  return b''


def index_post() -> bytes:
  return b''


callbacks = {
  'POST': index_post,
  'GET': index_get,
}


@attendees.route('/', methods=tuple(callbacks.keys()))
def index() -> Optional[bytes]:
  return callbacks[request.method]()