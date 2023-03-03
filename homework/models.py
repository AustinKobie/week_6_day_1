from datetime import datetime
from homework import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
class User(UserMixin, db.Model):
    id= db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(150), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)
    cars = db.relationship('Car', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return f'<User: {self.username}>' 
    
    def __str__(self):
        return f'User: {self.email}|{self.username}'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
    
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30))
    model = db.Column(db.String(50))
    year = db.Column(db.Date)
    color = db.Column(db.String(20))
    price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'<Car: {self.make}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()