import os


class Config:
  DATABASE_URI = os.environ.get('DATABASE_URI')


class DevelopmentConfig(Config):
  DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
  pass


class StagingConfig(Config):
  pass