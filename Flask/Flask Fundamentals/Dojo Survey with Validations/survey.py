from flask import Flask, render_template, request, redirect, session, flash #import flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    option_list = ['San Jose', 'New York', 'Seattle', 'Houston']
    language_list = ['Python', 'PHP', 'Javascript', 'Rails']
    return render_template('index.html', option_list=option_list, language_list=language_list)

@app.route('/create', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect ('/')
    if len(request.form['comment']) < 1:
        flash("Comment cannot be empty!")
        return redirect ('/')
    if len(request.form['comment']) > 120:
        flash("Comment cannot be more than 120 characters long!")
        return redirect ('/')
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
    return redirect('/process')

@app.route('/process')
def show_user():
    return render_template('results.html')

app.run(debug=True)