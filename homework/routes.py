from flask import render_template, flash, redirect 
from homework import homework, db
from homework.forms import RegisterForm, SignInForms, CarForm
from homework.models import User, Car
from flask_login import current_user, login_user, logout_user, login_required

@homework.route('/', methods=['GET','POST'])
def index():
      form = CarForm()
      if form.validate_on_submit():
            make = form.make.data
            model = form.model.data
            year = form.year.data
            color = form.color.data
            price = form.price.data
            c = Car(make=make, model=model, year=year, color=color, price=price)
            c.commit()
            flash(f'{form.make} accepted')
            return redirect('/')
      return render_template('index.jinja', form=form)

@homework.route('/about')
def about():
    return render_template('about.jinja')

@homework.route('/login', methods=['GET','POST'])
def login():
      form = SignInForms()
      if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user_match = User.query.filter_by(username=username).first()
            if not user_match or not user_match.check_password(password):
                  flash(f'Username or password was incorrect, try again')
                  return redirect('/login')
            flash(f'{username} successfully signed in')
            login_user(user_match, remember=form.remember_me.data)
            return redirect('/')
      return render_template('login.jinja', signin_form=form)

@homework.route('/signout')
@login_required
def sign_out():
      logout_user()
      return redirect('/')

@homework.route('/user/<username>')
def user(username):
      user_match = User.query.filter_by(username=username).first()
      if not user_match:
            redirect('/')
      cars = user_match.posts
      return render_template('user.jinja', user=user_match, posts=cars)

@homework.route('/register', methods=['GET','POST'])
def register():
      form = RegisterForm()
      if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            username = form.username.data
            email = form.email.data
            password = form.password.data
            u = User(first_name=first_name,last_name=last_name,username=username,email=email,password_hash='')
            user_match = User.query.filter_by(username=username).first()
            email_match = User.query.filter_by(email=email).first()
            if user_match:
                  flash(f'Username {username} already exists, try again')
                  return redirect('/register')            
            elif email_match:
                  flash(f'Email {email} already exists, try again')
                  return redirect('/register')
            else:
                  u.hash_password(password)
                  u.commit()
                  flash(f'Request to register {username} succesful')
                  return redirect('/')
            
      return render_template('register.jinja', form=form)

@homework.route('/blog')
def blog():
      return render_template('blog.jinja')