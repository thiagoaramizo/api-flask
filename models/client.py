from sqlalchemy import ForeignKey
from database import db
from models.user import User


class Client(db.Model):

    id = db.Column( db.String(50), primary_key=True )
    user_id = db.Column( ForeignKey(User.id) )
    name = db.Column( db.String(80), nullable=False )
    email = db.Column( db.String(100), nullable=True )
    cel = db.Column( db.String(100), nullable=True )
