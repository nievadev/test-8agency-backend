from typing import Optional

from flask import Blueprint, request, jsonify, make_response

import db
from .attendee_validator import AttendeeValidator


attendees = Blueprint('attendees', __name__)


def index_get() -> bytes:
  session = db.make_session()

  list_attendees = session.query(db.Attendee).all()

  return jsonify(list_attendees)


def index_post() -> bytes:
  data = request.get_json()

  authenticator = AttendeeValidator(data)

  if not authenticator.authenticated:
    return make_response(b'', 400)

  session = db.make_session()

  new_attendee = db.Attendee(
    name=data['name'],
    last_name=data['lastName'],
    work_email=data['workEmail'],
    country=data['country'],
    phone_number=data['phoneNumber'],
    work_position=data['workPosition']
  )

  session.add(new_attendee)

  session.commit()

  return jsonify(new_attendee)


callbacks = {
  'POST': index_post,
  'GET': index_get,
}


@attendees.route('/', methods=tuple(callbacks.keys()))
def index() -> Optional[bytes]:
  return callbacks[request.method]()