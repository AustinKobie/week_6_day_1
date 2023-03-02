from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


homework = Flask(__name__)
homework.config.from_object(Config)
db = SQLAlchemy(homework)
migrate = Migrate(homework, db)


from homework import routes, models