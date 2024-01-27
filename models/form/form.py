from sqlalchemy import ForeignKey
from database import db
from models.user import User


class Form(db.Model):

    id = db.Column( db.String(50), primary_key=True )
    user_id = db.Column( ForeignKey(User.id) )
    name = db.Column( db.String(80), nullable=False )
    description = db.Column( db.Text, nullable=True )
    privacy = db.Column( db.String(100), nullable=True )
    status = db.Column( db.Integer, nullable=True )
