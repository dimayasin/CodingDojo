from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key="tardis"


@app.route('/')
def index():
    
    return render_template("index.html")


@app.route('/dojo_servey',methods=['POST'])
def OutputForm():

    name=request.form['name']
    location=request.form['location']
    favorite=request.form['favorite']
    comment=request.form['comment']


    return render_template("dojo_survey.html", **locals())



app.run(debug=True)
