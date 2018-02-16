from flask import Flask, render_template, request, redirect ,session
app = Flask(__name__)
app.secret_key="tardis"


@app.route('/')
def index():
    if not 'counter'  in session:
        session['counter'] = 0

    
    return render_template("index.html", counter=session['counter'])


def Refreshing():
    if request.form['restart'] :
        session['counter'] = 0
    return render_template("/")

 



@app.route('/level1_yes')
def level1_yes():
    session['counter'] += 1
    
    return render_template('level1_yes.html')

@app.route('/level1_no')

def level1_no():
     return render_template("level1_no.html")





app.run(debug=True)
