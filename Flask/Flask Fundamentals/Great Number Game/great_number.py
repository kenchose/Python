from flask import Flask, render_template, redirect, request, session, flash
import random
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if 'number' in session:
        random_num = session['number']
        print session['number']
    else:
        session['number'] = random.randrange(0, 101)
        print session['number']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print request.form['guess']
    if int(request.form['guess']) < int(session['number']):
        flash('Too low. Try again')
        return redirect('/')
    if int(request.form['guess']) > int(session['number']):
        flash('Too high, try again')
        return redirect('/') 
    if int(request.form['guess']) == int(session['number']):
        flash('You win!')
        session.pop('number')
    else:
        return 'Too high. Try again'
    return redirect('/')


app.run(debug=True)