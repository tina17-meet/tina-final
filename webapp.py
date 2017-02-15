from flask import *
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func, DateTime
from flask import session as login_session
from werkzeug.utils import secure_filename
import locale, os

app = Flask(__name__)

Base = declarative_base()
engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


@app.route('/')
def homepage():
	return render_template('home.html')

@app.route('/biographies')
def biographies():
	return render_template('biographies.html')

@app.route('/facts')
def facts():
	return render_template('facts.html')

@app.route('/teams')
def teams():
	return render_template('teams.html')

@app.route('/aboutme')
def aboutme():
	return render_template('aboutme.html')




if __name__ == '__main__':
	app.run(debug = True)