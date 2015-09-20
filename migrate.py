from app.model import *

database.connect()
database.create_tables([User, Post])
