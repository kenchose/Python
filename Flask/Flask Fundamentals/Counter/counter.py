from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    # counter = 0
    if 'counter' in session:
        session['counter'] += 1
    else: 
        session['counter'] = 1
    print session['counter']
    return render_template('index.html', num = session['counter'])


app.run(debug=True)

