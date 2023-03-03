from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


homework = Flask(__name__)
homework.config.from_object(Config)
db = SQLAlchemy(homework)
migrate = Migrate(homework, db)
login = LoginManager(homework)

login.login_view='/login'
login.login_message="Make sure you log in"


from homework import routes, models