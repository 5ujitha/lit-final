from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    full_name = db.Column(db.String(150))

class User_profile(db.Model):
    u_id                 = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True,)
    u_type               = db.Column(db.String(20),primary_key=True)
    u_email              = db.Column(db.String(150), db.ForeignKey('user.email'))
    u_full_name          = db.Column(db.String(30),  db.ForeignKey('user.full_name'))
    u_schemes            = db.Column(db.String(150))
    u_firm               = db.Column(db.String(150))
    u_legalspeciality    = db.Column(db.String(150))
    u_img                = db.Column(db.String(150))
    u_legalservice       = db.Column(db.String(150))
    u_pricerange         = db.Column(db.String(150))
    u_description        = db.Column(db.String(3000))
    u_represent          = db.Column(db.String(150))
    u_accomplishment     = db.Column(db.String(3000))
    u_company            = db.Column(db.String(3000))
    


    