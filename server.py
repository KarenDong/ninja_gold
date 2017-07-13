from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key='ThisisSecret'

from datetime import datetime
from random import *

@app.route('/')
def index():
    session['time'] = str(datetime.now())
    return render_template('index.html')

@app.route('/process_money',methods=['GET','POST'])
def process_money():
    try:
        session['total_gold']
    except:
        session['total_gold'] = 0
    session['building'] = request.form['building']
    if session['building'] == "casino":
        session['gold'] = randint(-50,50)
        if session['gold'] > 0:
            session['display'] = 1
        else:
            session['display'] = 2
    elif session['building'] == "farm":
        session['gold'] = randint(10,20)
        session['display'] = 1
    elif session['building'] == "cave":
        session['gold'] = randint(5,10)
        session['display'] = 1
    elif session['building'] == "house":
        session['gold'] = randint(2,5)
    session['total_gold'] += session['gold']
    return redirect('/')

app.run(debug=True)
