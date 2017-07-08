from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = 'numbergame'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(0, 101)
        print session['number']
    return render_template('index.html')

@app.route('/', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    guess = int(session['guess'])
    answer = session['number']
    if guess > answer:
        flash('Too High!')
        css_style = 'wrong'
    elif guess < answer:
        flash('Too Low')
        css_style = 'wrong'
    else:
        flash('You won!')
        css_style = 'correct'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
