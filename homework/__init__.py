from flask import Flask
from config import Config


homework = Flask(__name__)
homework.config.from_object(Config)


from homework import routes