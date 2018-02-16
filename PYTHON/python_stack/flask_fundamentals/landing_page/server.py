from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ninjas')
def ninjas():
    print "Ninjas Page"
    return render_template("ninjas.html")


@app.route('/dojo')
def dojo():
    name= request.form['name']
    # # email = request.form['email']

    # print name
    # # print email


    return render_template('/dojo.html')



app.run(debug=True)
