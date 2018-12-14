from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secrete_key = 'secrete_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
        flash('All fields are required and must not be blank')
    return redirect('/')


#     session['email'] = request.form[]
#     session['first_name']
#     session['last_name']:
#     session['password':
#     session['confirmation_password']: 

app.run(debug=True)
