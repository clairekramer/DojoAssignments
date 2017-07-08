from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    img = 'img/tmnt.png'
    return render_template('ninja.html', img=img)

@app.route('/ninja/<ninjaColor>')
def ninjaColor(ninjaColor):
    if ninjaColor == 'blue':
        img = 'img/leonardo.jpg'
    elif ninjaColor == 'orange':
        img = 'img/michelangelo.jpg'
    elif ninjaColor == 'red':
        img = 'img/raphael.jpg'
    elif ninjaColor == 'purple':
        img = 'img/donatello.jpg'
    else:
        img = 'img/notapril.jpg'
    return render_template('ninja.html', img=img)

app.run(debug=True)
