from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template("index.html")


@app.route('/process',methods=['POST'])
def dojo():
    name= request.form['name']
    return render_template('/')



app.run(debug=True)
