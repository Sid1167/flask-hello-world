from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Hello.html')

@app.route('/about')
def about():
    return 'About'
