from flask import Flask, render_template, request, redirect, flash, session
app=Flask(__name__)
app.secret_key='dojo'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def surveyResult():
    print 'Got Post Info'

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(request.form['name']) < 1:
        flash('Please enter your Name.')
    elif len(request.form['comment']) < 1:
        flash('Please enter a comment')
    elif len(request.form['comment']) > 120:
        flash('Comment cannot be more than 120 characters')

    if len(name) < 1 or (len(comment) < 1 or len(comment) > 120):
        return redirect('/')

    return render_template('result.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)
