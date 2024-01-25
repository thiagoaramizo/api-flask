from database import db

class Client(db.Model):

    id = db.Column( db.String(50), primary_key=True )
    user = db.Column( db.String(50), nullable=False )
    name = db.Column( db.String(80), nullable=False )
    email = db.Column( db.String(100), unique=True, nullable=True )
    cel = db.Column( db.String(100), nullable=True )
