from flask import Flask, render_template,session, request, redirect
app = Flask(__name__)
app.secret_key = 'tardis'


@app.route('/')
def index():

    if not 'counter' in session:
        session['counter'] = 0
    session['counter'] += 1
  
    return render_template("index.html", counter=session['counter'])  

@app.route('/up')
def plus_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = -1
    return redirect('/')








app.run(debug=True)
