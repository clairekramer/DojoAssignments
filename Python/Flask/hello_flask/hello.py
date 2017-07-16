from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name = 'Claire', times=6, phase= 'Hello')

app.run(debug=True)
