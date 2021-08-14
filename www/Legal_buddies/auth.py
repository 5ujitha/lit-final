from datetime import timedelta
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, User_profile
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('full_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(full_name) < 2:
            flash('Full name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, full_name= full_name, password= password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.presign_up'))

    return render_template("sign_up.html",user=current_user)


@auth.route('/presign_up',methods=['GET', 'POST'])
def presign_up():
    if request.method == 'POST':
        typeOfUser = request.form.get('type')
        if len(typeOfUser)  > 1 :
            return redirect(url_for('views.createprofile',title = typeOfUser,user=current_user))
       
    return redirect(url_for('views.presign_up'))




@auth.route('/createprofile/<title>',methods=['GET', 'POST'])
def processing_profile(title):

    if request.method == 'POST':
        u_id = current_user.id
        u_type = title
        u_email = request.form.get('user_email')
        u_full_name = request.form.get('user_full_name')
        u_schemes= request.form.get('user_schemes')
        u_legalspeciality = request.form.get('user_legalspeciality')
        u_img = request.form.get('picture')
        u_legalservice = request.form.get('user_legalservice')
        u_pricerange = request.form.get('user_pricerange')
        u_firm = request.form.get('user_firm')
        u_company = request.form.get('user_company')
        u_description = request.form.get('user_description')
        u_represent = request.form.get('user_represent')
        u_accomplishment = request.form.get('user_accomplishment')
        


        
        if u_type == "Lawyer" :
            
            new_user_profile = User_profile(u_id = u_id, 
                                            u_type = u_type,
                                            u_email = u_email, 
                                            u_full_name = u_full_name , 
                                            u_schemes = u_schemes, 
                                            u_legalspeciality = u_legalspeciality,
                                            u_firm = u_firm,
                                            u_img = u_img,
                                            u_legalservice = "null" , 
                                            u_description = "null",
                                            u_accomplishment = u_accomplishment,
                                            u_company = u_company,
                                            u_represent = "null",
                                            u_pricerange = "null")
            db.session.add(new_user_profile)
            db.session.commit()
            return redirect(url_for("views.display_user_profile" ))

        else:
            new_user_profile = User_profile(u_id = u_id, 
                                                u_type = u_type,
                                                u_email = u_email, 
                                                u_full_name = u_full_name , 
                                                u_legalservice = u_legalservice ,
                                                u_represent = u_represent,
                                                u_pricerange = u_pricerange,
                                                u_description = u_description,
                                                u_schemes = u_schemes, 
                                                u_legalspeciality = "null",
                                                u_accomplishment = "null",
                                                u_firm = "null",
                                                u_company = "null",
                                                u_img = "null")
                                            
            db.session.add(new_user_profile)
            db.session.commit()

            return redirect(url_for("views.display_user_profile" ))
            
    
   

    
 
@auth.route('/swipe')
def swipe():
    return redirect(url_for('views.swipe'))

@auth.route('/approvedlist')
def approvedlist():
    return redirect(url_for('views.approvedlist'))

@auth.route('/schemes')
def schemes():
    return render_template("schemes.html",user=current_user)

@auth.route('/fees')
def fees():
    return render_template("fees.html",user=current_user)


@auth.route('/procedure')
def procedure():
    return render_template("procedure.html",user=current_user)

