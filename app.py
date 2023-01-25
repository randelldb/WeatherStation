import os
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# set base dir
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Setup config key
app.config['SECRET_KEY'] = 'a super random key'

# Setup database connection
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create database model
class Sensors(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	type = db.Column(db.String(200), nullable=False)
	brand = db.Column(db.String(200), nullable=True)
	address = db.Column(db.Integer, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
@app.route('/index')
def index():
	title = 'Dashboard'
	return render_template('index.html', title=title)

@app.route('/sensors', methods=['POST', 'GET'])
def sensors():
	title = 'Sensors'

	if request.method == 'POST':
		flash("Form submitted")
		sensor_name = request.form['sensor_name']
		sensor_type = request.form['sensor_type']
		sensor_brand = request.form['sensor_brand']
		sensor_adress = request.form['sensor_adress']
		new_sensor = Sensors(name=sensor_name, type=sensor_type, brand=sensor_brand, address=sensor_adress)

		# push to database
		try:
			db.session.add(new_sensor)
			db.session.commit()
			return redirect('/sensors')
		except:
			return "Error"

	else:
		sensors = Sensors.query.order_by(Sensors.date_created)
		return render_template('sensors.html', title=title, sensors=sensors)

@app.route('/update_sensor/<int:id>', methods=['POST', 'GET'])
def update_sensor(id):
	sensor_to_update = Sensors.query.get_or_404(id)

	if request.method == 'POST':
		sensor_to_update.name = request.form['sensor_name']
		try:
			db.session.commit()
			return redirect('/sensors')
		except:
			return 'error updating'
	else:
		return render_template('update_sensor.html', sensor_to_update=sensor_to_update)

@app.route('/delete_sensor/<int:id>')
def delete_sensor(id):
	sensors_to_delete = Sensors.query.get_or_404(id)

	try:
		db.session.delete(sensors_to_delete)
		db.session.commit()
		return redirect('/sensors')
	except:
		return 'delete error'

if __name__ == '__main__':
	app.run(debug=True)