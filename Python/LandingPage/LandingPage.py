from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')

def partOne():
    return render_template('index.html')

@app.route('/ninjas')

def partTwo():
    print "Displaying Ninja Info"
    return redirect('/')

@app.route('/dojos/new')

def partThree():
    print 'Displaying Form'
    return redirect('/')

app.run(debug=True)
