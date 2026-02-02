# Where we define our authentication-related routes and logic.
from flask import Blueprint, redirect, url_for, render_template, request, session, flash
from models import db, users

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['nm']
        email = request.form.get('email', '')
        session['user'] = user
        session['email'] = email
        
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            flash("User already exists!", "info")
        else:
            new_user = users(user, email)
            db.session.add(new_user)
            db.session.commit()
        
        flash("You have been logged in!", "success")
        return redirect(url_for('auth.user'))
    
    else:
        if 'user' in session:
            flash("Already logged in!", "info")
            return redirect(url_for('auth.user'))
        return render_template('login.html')

@auth_bp.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if 'user' in session:
        user = session['user']
        
        if request.method == "POST":
            email = request.form['email']
            flash("Email was saved!", "success")
            session['email'] = email
        else:
            if 'email' in session:
                email = session['email']
        
        return render_template('user.html', email=email)
    else:
        flash("You are not logged in!", "warning")
        return redirect(url_for('auth.login'))

@auth_bp.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('auth.login'))