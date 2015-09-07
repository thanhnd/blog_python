from base import *

class User(BaseModel):
    email = CharField(unique = True)
    password = CharField()

class Post(BaseModel):
    title = CharField()
    content = CharField()
    created_date = DateTimeField()
