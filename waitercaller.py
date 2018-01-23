# coding:utf-8
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from mockdbhelper import MockDBHelper as DBHelper
from user import User
from passwordhelper import PasswordHelper
from bitlyhelper import BitlyHelper
import config
import datetime
from forms import RegistrationForm

DB = DBHelper()
PH = PasswordHelper()
BH = BitlyHelper()

app = Flask(__name__)
app.secret_key = 'vwJFwvqaFZIkqqkqE4PWGFTQyWvOfbI/aqOSshz/XQbh/PX3cZfVKBqwk59QiUp79h/lg410yvB9Vldynz1yL9qTBiz/EWqtCQi'
login_manager = LoginManager(app)

@app.route('/')
def home():
    registrationform = RegistrationForm()
    return render_template('home.html', registrationform=registrationform)

@app.route('/account')
@login_required
def account():
    tables = DB.get_tables(current_user.get_id())
    return render_template('account.html',tables=tables)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    stored_user = DB.get_user(email)
    if stored_user and PH.validate_password(password, stored_user['salt'], stored_user['hashed']):
        user = User(email)
        login_user(user,remember=True)
        return redirect(url_for('account'))

@login_manager.user_loader
def load_user(user_id):
    user = DB.get_user(user_id)
    if user:
        return User(user_id)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    pw1 = request.form.get('password')
    pw2 = request.form.get('password2')
    if not pw1 == pw2:
        return redirect(url_for('home'))
    if DB.get_user(email):
        return redirect(url_for('home'))
    salt = PH.get_salt()
    print(pw1, salt)
    hashed = PH.get_hash(pw1 + salt)
    DB.add_user(email, salt, hashed)
    return redirect(url_for('home'))

@app.route('/account/createtable', methods=['POST'])
@login_required
def account_createtable():
    # customer input table id
    tablename = request.form.get('tablenumber')
    # unique globals table id
    tableid = DB.add_table(tablename, current_user.get_id())
    new_url = BH.shorten_url(config.base_url+'newrequest/'+tableid)
    DB.update_table(tableid, new_url)
    return redirect(url_for('account'))

@app.route('/account/deletetable')
@login_required
def account_deletetable():
    tableid = request.args.get('tableid')
    DB.delete_table(tableid)
    return redirect(url_for('account'))

@app.route('/newrequest/<tid>')
def new_request(tid):
    DB.add_request(tid, datetime.datetime.now())
    return 'Your request has been logged and a waiter will be with you shortly'

@app.route('/dashboard')
@login_required
def dashboard():
    now = datetime.datetime.now()
    requests = DB.get_request(current_user.get_id())
    for req in requests:
        deltaseconds = (now - req['time']).seconds
        req['wait_minutes'] = "{}.{}".format(int(deltaseconds/60), str(deltaseconds % 60).zfill(2))
    return render_template('dashboard.html', requests=requests)

@app.route('/dashboard/resolve')
@login_required
def dashboard_resolve():
    request_id = request.args.get('request_id')
    DB.delete_request(request_id)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)