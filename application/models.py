import flask
from application import db

class videopop(db.Document):
    courseID   =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=255 )
    credits     =   db.IntField()
    term        =   db.StringField( max_length=25 )