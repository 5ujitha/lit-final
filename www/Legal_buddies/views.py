from re import S
from flask import Blueprint, app, render_template, request, flash, jsonify ,redirect, url_for
from flask_login import login_required, current_user
from .models import User_profile
from . import db
import json
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

from functools import wraps
import os



views = Blueprint('views', __name__)



@views.route('/')
@login_required
def home():
    email = current_user.email
    get_type = User_profile.query.filter_by(u_email=email).first()
    current_user_profile = User_profile.query.where(User_profile.u_email!=email)
    return render_template('home.html', user = current_user, current_user_profile = current_user_profile ,type = get_type.u_type)


@views.route('/createprofile/<title>') 
@login_required
def createprofile(title):
    return render_template("createprofile.html",title=title,user=current_user)




@views.route('/presign_up')  
@login_required
def presign_up():
    return render_template("presign_up.html",user=current_user)

@views.route('/my_profile')
@login_required
def display_user_profile():
    email = current_user.email
    current_user_profile = User_profile.query.filter_by(u_email=email)
    #cur.execute("""SELECT * FROM user_profile WHERE u_email = %s""", (email,))
    #user = cur.fetchone()
    return render_template('my_profile.html', user = current_user, current_user_profile = current_user_profile)


@views.route('/swipe')
@login_required
def display_users():
    email = current_user.email
    get_type = User_profile.query.filter_by(u_email=email).first()
    
    current_user_profile = User_profile.query.where(User_profile.u_email!=email)
    
    #current_user_profile = User_profile.query.from_statement(db.text(("""SELECT * FROM user_profile WHERE u_email != %s""", (email,))))
    #cur.execute("""SELECT * FROM user_profile WHERE u_email = %s""", (email,))
    #user = cur.fetchone()
    return render_template("swipe.html", user = current_user, current_user_profile = current_user_profile ,type = get_type.u_type)


@views.route('/approvedlist')
@login_required
def display_usersapproved():
    email = current_user.email
    get_type = User_profile.query.filter_by(u_email=email).first()
    
    current_user_profile = User_profile.query.where(User_profile.u_email!=email)
    
    #current_user_profile = User_profile.query.from_statement(db.text(("""SELECT * FROM user_profile WHERE u_email != %s""", (email,))))
    #cur.execute("""SELECT * FROM user_profile WHERE u_email = %s""", (email,))
    #user = cur.fetchone()
    return render_template("approvedlist.html", user = current_user, current_user_profile = current_user_profile ,type = get_type.u_type)


@views.route('/my_profile/<id>/<type>/<email>/<full_name>/<legalservice>/<legalspeciality>/<firm>/<pricerange>/<schemes>/<img>/<represent>/<description>')  
@login_required
def my_profile(id,type,email,full_name,legalservice, legalspeciality,firm,pricerange,schemes,img, certificate, accomplishment, company):
    return render_template("my_profile.html",    
                                            id =id, 
                                            type =type , 
                                            email = email , 
                                            full_name = full_name ,
                                            legalservice = legalservice,
                                            legalspeciality = legalspeciality,
                                            firm = firm,
                                            pricerange = pricerange,
                                            schemes = schemes,
                                            img = img      ,   
                                            user=current_user,
                                            represent = represent,
                                            description = description,
                                            accomplishment = accomplishment,
                                            certificate = certificate,
                                            company = company
                                            )



