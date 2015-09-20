from app.models import *

database.connect()
database.create_tables([User, Post])
