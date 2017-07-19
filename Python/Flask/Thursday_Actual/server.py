from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product', methods=['POST'])
def product():
    print request.form['product_name']
    session['product_info'] = request.form
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
