from peewee import *

database = SqliteDatabase("blog.db")

class BaseModel(Model):
    class Meta:
        database = database
