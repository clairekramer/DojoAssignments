from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    img = 'tmnt.png'
    return render_template('ninja.html', img=img)

@app.route('/ninja/<ninja_color>')
def ninja_color(ninja_color):
    if ninja_color == 'blue':
        img = 'leonardo.jpg'
        print 'Showing Leonardo'
    elif ninja_color == 'orange':
        img = 'michelangelo.jpg'
    elif ninja_color == 'red':
        img = 'raphael.jpg'
    elif ninja_color == 'purple':
        img = 'donatello.jpg'
    else:
        img = 'notapril.jpg'
    return render_template('ninja.html', img=img)

app.run(debug=True)
