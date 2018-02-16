from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key="tardis"


@app.route('/')
def index():
    
    return render_template("index.html")


@app.route('/dojo_servey',methods=['POST'])
def OutputForm():
    session['full_name']= request.form['name']
    session['dojo_location']= request.form['location']
    session['favorite']= request.form['favorite']
    session['comment']= request.form['comment']
    return render_template("dojo_survey.html")



app.run(debug=True)
