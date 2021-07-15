from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ian:alex@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://txpodqbtkclkxf:726b2baff5ac60f342c6416a2b25f51ca2d2a2099358274936736a01859b5c5c@ec2-54-220-53-223.eu-west-1.compute.amazonaws.com:5432/d1nvb11q0tanr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

class Favqoutes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favqoutes.query.all()
    return render_template('index.html', result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    
    quotedata = Favqoutes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    
    return redirect(url_for('index'))
