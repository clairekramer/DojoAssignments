from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def survey():
    print request.form['name']
    session['survey_results'] = request.form
    if len(request.form['name']) < 1:
        flash('Name cannot be empty!')
        return redirect('/')
    else:
        flash('Success! Your name is {}'.format(request.form['name']))
    if len(request.form['comment']) > 120:
        flash('Comment cannot be longer than 120 characters!')
        return redirect('/')
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

app.run(debug=True)
