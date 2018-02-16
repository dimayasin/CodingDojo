from flask import Flask, render_template,session, request, redirect
app = Flask(__name__)
app.secret_key = 'tardis'

import random
import datetime

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
        session['msg'] = ""
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def myGuess():
    Value = request.form['building']
    # print type(Value)


    game_time=datetime.datetime.fromtimestamp(1518377161).isoformat()
    if  Value == "farm" :
        session['gold'] += random.randrange(10,21)
        session['msg'] ="Earned "+str(session['gold'])+" golds from the farm!"+str(game_time)
    elif Value == "cave" :
        session['gold'] += random.randrange(5,11)
        session['msg'] ="Earned "+str(session['gold'])+" golds from the farm!"+str(game_time)
    elif Value == "house" :
        session['gold'] += random.randrange(2,6)
        session['msg'] ="Earned "+str(session['gold'])+" golds from the farm!"+str(game_time)
    elif Value == "casino" :
        session['gold'] += random.randrange(-50,51)
        session['msg'] ="Earned "+str(session['gold'])+" golds from the farm!"+str(game_time)
  
    return redirect("/")  



@app.route('/reset', methods=['POST'])
def RestingGame():
    
    session['gold'] = 0
    session['msg'] = ""
    return redirect("/")




app.run(debug=True)
