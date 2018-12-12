from flask import Flask, render_template, redirect, session, request
import random
from datetime import datetime 
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if 'number' in session:
        session['gold'] = 0
    if 'message' in session:
        session['message_board'] = []
    return render_template('index.html') 

@app.route('/process', methods=['POST'])
def process():
    if request.form['action'] == 'farm':
        amt = random.randrange(10, 21)
        date = datetime.now().strftime("%Y/%m/%d at %I:%M%p")
        activity = "Earned {} golds from the farm! ({})".format(amt, date)

    elif request.form['action'] == 'cave':
        amt = random.randrange(5, 11)
        date = datetime.now().strftime("%Y/%m/%d at %I:%M%p")
        activity = "Earned {} golds from the cave! ({})".format(amt, date)  

    elif request.form['action'] =='house':
        amt = random.randrange(2, 6)
        date = datetime.now().strftime("%Y/%m/%d at %I:%M%p")
        activity = "Earned {} golds from the house! ({})".format(amt, date)

    elif request.form['action'] == 'casino':
        amt = random.randrange(-50, 51)
        date = datetime.now().strftime("%Y/%m/%d at %I:%M%p")
        if amt < 0:
            activity = "Entered a casino and lost {} golds...ouch!".format(amt)

        elif amt > 0:
            activity = "Entered a casino and earned {} golds!".format(amt)

        elif amt == 0:
            activity = "Entered a casino and didn't lose any gold. Hey, it's better than losing"
        
    session['gold'] += amt
    curr_message = session['message_board']
    curr_message.append(activity)
    session['message_board'] = curr_message
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    session['gold'] = 0
    session['message_board'] = []
    return redirect('/')
app.run(debug=True)