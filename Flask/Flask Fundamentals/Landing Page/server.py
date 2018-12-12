from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def landing_template():
    return render_template('index.html')

@app.route('/ninjas')
def ninja_tempolate():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojo_form():
    return render_template('dojos.html')
app.run(debug = True)