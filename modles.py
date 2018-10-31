#  Defining the classes for the Database
from app import db 
from datetime import datetime
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    username=db.Column(db.String(25), unique=True , nullable=False)
    email=db.Column(db.String(25), unique=True , nullable=False)
    password=db.Column(db.String(25) , nullable=False)
    image_file=db.Column(db.String(25), nullable=True , default='default.jpg')

def __repr__(self):
    return f" '{self.username}','{self.email}','{self.image_file}' "



#  Defining the Model Post Modle 

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    title=db.Column(db.String(100) , nullable=False)
    body=db.Column(db.Text , nullable=False  )
    date_posted=db.Column(db.DateTime ,nullable=False , default=datetime.utcnow)


def __repr__(self):
    return f"'{self.title}' , '{self.date_posted}'"
