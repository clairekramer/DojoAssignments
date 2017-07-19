from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = "numbergame"

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(0,101)
    print session['number']
    return render_template('index.html')

@app.route('/', methods=['POST'])
def guess():
    print request.form['guess']
    session['guess'] = int(request.form['guess'])
    guess = int(session['guess'])
    answer = session['number']
    if guess > answer:
        session['result'] = 'high'
        session['response'] = 'wrong'
    elif guess < answer:
        session['result'] = 'low'
        session['response'] = 'wrong'
    else:
        message = flash('You Won!')
        session['response'] = 'correct'
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
