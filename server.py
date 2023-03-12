from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'password123'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    if 'activitylog' not in session:
        session['activitylog']=""
    return render_template('index.html')

@app.route('/process_money', methods=['post'])
def process():
    if request.form['building']=='farm':
        x = random.randint(10,20)
        session['gold'] += x
        session['activitylog'] = f'<p class="green margin-top-10">Earned {x} gold from the farm!</p>'+session['activitylog']
    elif request.form['building']=='cave':
        x = random.randint(5,10)
        session['gold'] += x 
        session['activitylog'] = f'<p class="green margin-top-10">Earned {x} gold from the cave!</p>'+session['activitylog']
    elif request.form['building']=='house':
        x = random.randint(2,5)
        session['gold'] += x
        session['activitylog'] = f'<p class="green margin-top-10">Earned {x} gold from the house!</p>'+session['activitylog']
    elif request.form['building']=='casino':
        x = random.randint(-50,50)
        session['gold'] += x
        if x>=0:
            session['activitylog'] = f'<p class="green margin-top-10">Entered a casino and won {x} gold!</p>'+session['activitylog']
        else:
            session['activitylog'] = f'<p class="red margin-top-10">Entered a casino and lost {x*-1} gold... Ouch.</p>'+session['activitylog']
    return redirect('/')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
    
if __name__=='__main__':
    app.run(debug=True)