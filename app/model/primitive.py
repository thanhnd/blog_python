from datetime import datetime
from base import *

class User(BaseModel):
    email = CharField(unique = True)
    password = CharField()

class Post(BaseModel):
    title = CharField()
    content = CharField()
    created_date = DateTimeField(default = datetime.now)
    author = ForeignKeyField(User, related_name = 'posts')
