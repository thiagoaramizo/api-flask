from sqlalchemy import ForeignKey
from database import db
from models.form.form import Form


class Label(db.Model):

    id = db.Column( db.String(50), primary_key=True )
    form_id = db.Column( ForeignKey(Form.id) )
    name = db.Column( db.String(200), nullable=False )
    input = db.Column( db.String(20), nullable=False )
    order = db.Column( db.Integer, nullable=True  )
    description =  db.Column( db.Text, nullable=True )
    required =  db.Column( db.Integer, nullable=False )
    options = db.Column( db.Text, nullable=True )
    status = db.Column( db.Integer, nullable=True )
