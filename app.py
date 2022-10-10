from multiprocessing import context
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


base_dir = os.path.dirname(os.path.realpath(__file__))
# print(base_dir)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(base_dir, 'users.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model): #user
 __tablename__= 'user'
 id = db.Column(db.Integer(), primary_key=True)
 username = db.Column(db.String(255), nullable=False)
 email = db.Column(db.String(40), nullable=False)
 age = db.Column(db.Integer(), nullable=False)
 gender = db.Column(db.String(50), nullable=False)
  #  this returns string repesentation of objects in a db
 def __repr__(self):
  return f"User {self.username}"

 


@app.route('/')
def index():
  users=User.query.all()
  
  context={
    'users':users 
  }
  return render_template('models.html', **context)


# @app.route('/update/<int:id>')
# def update():
#  pass
# #  return render_template('update.html')


if __name__ == "__main__":
  app.run(debug=True)