from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'counter'

@app.route('/')
def index():
    try:
        session['count'] += 1
    except KeyError:
        session['count'] = 1
    return render_template('index.html')

app.run(debug=True)
