from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = 'RegForm'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/', methods=['GET'])
def index():
    if 'users' not in session:
        session['users'] = []
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
    error = True
    password = request.form['password']
    confirm = request.form['confirm']
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm']) < 1:
        flash('All fields of the form are required.')
        error = False
    elif str.isalpha(str(request.form['first_name'])) == False or str.isalpha(str(request.form['last_name'])) == False:
        flash('Names can only contain letters')
        error = False
    elif len(request.form['password']) < 8:
        flash('Password must contain at least 8 characters.')
        error = False
    elif password != confirm:
        flash('Password does not match.')
        error = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!')
        error = False
    if error == False:
        return redirect('/')
    else: #create new user
        user = {
            'first_name' : str(request.form['first_name']),
            'last_name' : str(request.form['last_name']),
            'email' : str(request.form['email']),
            'password' : str(request.form['password'])
        }

        session['users'].append(user)
        flash('Successfully Registered!')
        return redirect('/')

app.run(debug=True)
