from sqlalchemy import ForeignKey
from database import db
from models.form.label import Label
from models.client import Client


class Answer(db.Model):

    id = db.Column( db.String(50), primary_key=True )
    label_id = db.Column( ForeignKey(Label.id) )
    client_id = db.Column( ForeignKey(Client.id) )

    created_at = db.Column( db.Date )
    edited_at = db.Column( db.Date )
    status = db.Column( db.Integer, nullable=False )

    text = db.Column( db.Text, nullable=True )
    number = db.Column( db.Integer, nullable=True )
    float_number = db.Column( db.Float, nullable=True )
    bollean = db.Column( db.Integer, nullable=True )
    