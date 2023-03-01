from flask import render_template, flash, redirect 
from homework import homework
from homework.forms import RegisterForm, SignInForms, CarForm

@homework.route('/', methods=['GET','POST'])
def index():
      form = CarForm()
      if form.validate_on_submit():
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
            flash(f'Request to register {form.username} succesful')
            return redirect('/')
      return render_template('register.jinja', form=form)

@homework.route('/blog')
def blog():
      return render_template('blog.jinja')