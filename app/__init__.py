# coding:utf8
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/movie_project"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = '123456'
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
app.debug = True
db = SQLAlchemy(app)
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 前台
app.register_blueprint(home_blueprint)
# 后台
app.register_blueprint(admin_blueprint, url_prefix='/admin')


# 404错误页面
@app.errorhandler(404)
def page_no_found(error):
    return render_template('home/404.html'), 404
