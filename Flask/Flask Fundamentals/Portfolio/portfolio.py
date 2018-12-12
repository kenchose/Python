from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def my_portfolio():
    return render_template('My_Portfolio.html')

@app.route('/projects')
def web_page():
    return render_template('A_Web_Page.html')
    
@app.route('/about')
def about():
    return render_template('about_me.html')

app.run(debug=True)