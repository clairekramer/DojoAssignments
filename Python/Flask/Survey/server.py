from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def survey():
    print request.form['name']
    session['survey_results'] = request.form
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

app.run(debug=True)
