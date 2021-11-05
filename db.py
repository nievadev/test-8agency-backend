import os
from dataclasses import dataclass

import dotenv
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, create_engine, BigInteger, String
from sqlalchemy.orm.session import Session


dotenv.load_dotenv()

connection = create_engine(os.environ.get('DATABASE_URL'), future=True)

Base: DeclarativeMeta = declarative_base()


def make_session(*args: str) -> Session:
  return sessionmaker(connection)(*args)


@dataclass
class Attendee(Base):
  name: str
  last_name: str
  work_position: str

  __tablename__ = 'attendees'

  id = Column(BigInteger(), primary_key=True)
  name = Column(String(50), nullable=False, unique=False)
  last_name = Column(String(50), nullable=False, unique=False)
  work_email = Column(String(50), nullable=False, unique=False)
  phone_number = Column(String(50), nullable=False, unique=False)
  country = Column(String(50), nullable=False, unique=False)
  work_position = Column(String(50), nullable=False, unique=False)


Base.metadata.create_all(connection)
