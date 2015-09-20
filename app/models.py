from peewee import *
from datetime import datetime

database = SqliteDatabase("blog.db")

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    email = CharField(unique = True)
    password = CharField()

class Post(BaseModel):
    title = CharField()
    content = CharField()
    created_date = DateTimeField(default = datetime.now)
    author = ForeignKeyField(User, related_name = 'posts')
