from flask import Flask, render_template,session, request, redirect
app = Flask(__name__)
app.secret_key = 'tardis'

import random

@app.route('/')
def index():
    if not 'number' in session:
        session['number'] = 0
        session['msg'] = ""
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def myGuess():
    mynumber = int(request.form['number'])
    
    if  mynumber > 100:
        session['msg'] ="Too High!"
    elif mynumber < 0:
        session['msg'] ="Too Low!"
 
    if mynumber == random.randrange(0,101):
        session['msg'] =str(mynumber)+" was the right number!"
    else:
        session['msg'] = str(mynumber)+" was not the right number."
    session['number'] = mynumber
  
    return redirect("/")  








app.run(debug=True)
