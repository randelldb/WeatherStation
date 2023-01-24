import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init database
db = SQLAlchemy(app)

# Create database model
class Sensors(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	type = db.Column(db.String(200), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	# # Create return fn
	# def __repr__(self):
	# 	return '<Name %r>' % self.id

@app.route("/")
@app.route("/index")
def index():
	title = "Dashboard"
	return render_template("index.html", title=title)

@app.route("/sensors")
def sensors():
	title = "Sensors"
	return render_template("sensors.html", title=title)

if __name__ == '__main__':
	app.run(debug=True)