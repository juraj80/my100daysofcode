import sqlalchemy
import datetime

# noinspection PyPackageRequirements
from models.model_base import ModelBase


class Player(ModelBase):

    # def __init__(self):
    #     self.name = None
    __tablename__ = 'players'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)