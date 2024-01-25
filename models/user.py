from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):

    id = db.Column( db.String(50), primary_key=True )
    username = db.Column( db.String(80), unique=True, nullable=False )
    email = db.Column( db.String(100), unique=True, nullable=False )
    password = db.Column( db.String(100), nullable=False )

