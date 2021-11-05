import re
from pathlib import Path

import pycountry


country_hash = {country.name: True for country in pycountry.countries}

# Getting the pattern this way because it's too large
work_email_re_location = str(Path(__file__).absolute().parent / 'work_email_re')

with open(work_email_re_location, 'r') as file:
  work_email_re = re.compile(file.read())

phone_number_re = re.compile(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')


def validate_attendee(data: dict) -> bool:
  try:
    if type(data['name']) != str:
      return False

    elif type(data['workEmail']) != str:
      return False

    elif type(data['lastName']) != str:
      return False

    elif type(data['phoneNumber']) != str:
      return False

    elif type(data['workPosition']) != str:
      return False

    elif type(data['country']) != str:
      return False

    elif len(data['country']) > 50:
      return False

    elif len(data['workPosition']) > 50:
      return False

    elif len(data['lastName']) > 50:
      return False

    elif len(data['workEmail']) > 50:
      return False

    elif len(data['name']) > 50:
      return False

    elif len(data['phoneNumber']) > 50:
      return False

    elif not phone_number_re.match(data['phoneNumber']):
      return False

    elif not work_email_re.match(data['workEmail']):
      return False

    elif not country_hash.get(data['country'], False):
      return False

  except KeyError:
    return False

  return True


class AttendeeValidator:

  def __init__(self, data: dict) -> None:
    self._authenticated = validate_attendee(data)


  @property
  def authenticated(self) -> bool:
    return self._authenticated