from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lunathedog' \
                                            '@localhost/Wellness'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cbqtzztgosjtes:fcab08fb6c3285cca5548c1ab604c25690f0d5d5b8237e57528eaaf6ab4dd182' \
                                            '@ec2-54-159-112-44.compute-1.amazonaws.com:5432/d4oo4df55qr2q0'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Wellness(db.Model):
    __tablename__ = 'Wellness_v3'
    time = db.Column(db.DateTime(timezone=False), primary_key=True)
    name = db.Column(db.String(100))
    sleep = db.Column(db.Integer)
    meals = db.Column(db.Integer)
    work = db.Column(db.Integer)
    exercise = db.Column(db.Integer)
    meditation = db.Column(db.Integer)
    happiness = db.Column(db.Integer)

    def __init__(self, time,name,sleep,meals,work,exercise,meditation,happiness):
        self.time = time
        self.name = name
        self.sleep = sleep
        self.meals = meals
        self.work = work
        self.exercise = exercise
        self.meditation = meditation
        self.happiness = happiness

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method =='POST':
        time = datetime.now()
        name = request.form['name']
        sleep = request.form['Hours of sleep']
        meals = request.form['Number of meals']
        work = request.form['Number of work hours']
        try:
            exercise = request.form['Exercise check']
        except:
            pass
        try:
            meditation = request.form['Meditation check']
        except:
            pass
        try:
            happiness = request.form['Happiness']
        except:
            return render_template('index.html', message = 'Please enter all fields!')
        if name == '' or sleep == '' or meals == '' or work == '' or happiness == '':
            return render_template('index.html', message = 'Please enter all fields!')

        data = Wellness(time,name,sleep,meals,work,exercise,meditation,happiness)
        db.session.add(data)
        db.session.commit()
        send_mail(time,name,sleep,meals,work,exercise,meditation,happiness)
        return render_template('Success.html')

if __name__ == '__main__':

    app.run()