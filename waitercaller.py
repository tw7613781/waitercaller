# coding:utf-8
from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, login_user, logout_user

from mockdbhelper import MockDBHelper as DBHelper
from user import User

DB = DBHelper()

app = Flask(__name__)
app.secret_key = 'vwJFwvqaFZIkqqkqE4PWGFTQyWvOfbI/aqOSshz/XQbh/PX3cZfVKBqwk59QiUp79h/lg410yvB9Vldynz1yL9qTBiz/EWqtCQi'
login_manager = LoginManager(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/account')
@login_required
def account():
    return 'You are logged in'

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user_password = DB.get_user(email)
    if user_password and user_password == password:
        user = User(email)
        login_user(user,remember=True)
        return redirect(url_for('account'))

@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)