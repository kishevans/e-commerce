from flask import redirect, url_for, render_template, Blueprint
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from forms import *
from database.models import *

auth = Blueprint('auth',__name__)



@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()  #meta={'csrf':False}
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return(redirect(url_for('dashboard')))
        return '<h1>Invalid username or password</h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    return render_template('login.html', form=form)

@auth.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return '<h1>' + 'new user created' + '</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data +  ' ' + form.password.data +'</h1>'
    return render_template('signup.html', form=form)

@auth.route('/logout')
# @login_required
def logout():
    logout_user()
    return render_template('index.html')