from flask import render_template 
from homework import homework

@homework.route('/')
def index():
      return render_template('/index.jinja')

@homework.route('/about')
def about():
    return render_template('about.jinja')

@homework.route('/login')
def login():
      return render_template('login.jinja')

@homework.route('/register')
def register():
      return render_template('register.jinja')

@homework.route('/blog')
def blog():
      return render_template('blog.jinja')