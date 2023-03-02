from flask import render_template, flash, redirect 
from homework import homework, db
from homework.forms import RegisterForm, SignInForms, CarForm
from homework.models import User, Car

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
            flash(f'{form.car} accepted')
            return redirect('/')
      return render_template('index.jinja', form=form)

@homework.route('/about')
def about():
    return render_template('about.jinja')

@homework.route('/login', methods=['GET','POST'])
def login():
      form = SignInForms()
      if form.validate_on_submit():
            flash(f'{form.username} successfully signed in')
            return redirect('/')
      return render_template('login.jinja', signin_form=form)

@homework.route('/register', methods=['GET','POST'])
def register():
      form = RegisterForm()
      if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            username = form.username.data
            email = form.email.data
            password = form.password.data
            u = User(first_name=first_name,last_name=last_name,username=username,email=email,password_hash=password)
            u.commit()
            flash(f'Request to register {form.username} succesful')
            return redirect('/')
      return render_template('register.jinja', form=form)

@homework.route('/blog')
def blog():
      return render_template('blog.jinja')