from flask import Flask, render_template, url_for, redirect, current_app
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required, logout_user, current_user
from flask_migrate import Migrate

from forms import *
from database.models import *
from config import config



app = Flask(__name__)
app.config.from_object(config['development'])
db.init_app(app)

Bootstrap(app)
migrate = Migrate(app,db)

from auth.auth import auth
app.register_blueprint(auth)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)



if __name__ == '__main__':
   app.run(debug=True)