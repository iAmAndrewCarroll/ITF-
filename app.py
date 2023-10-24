from flask import Flask, render_template, session, request, redirect, url_for
import random
import os
from dotenv import load_dotenv
from flashcards_data import questions_and_answers

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route("/menu", methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        session_length = request.form.get('session_length')
        print("Session Length:", session_length)
        if session_length == "0":  # All cards
            session['cards'] = questions_and_answers.copy()
        else:
            session['cards'] = random.sample(questions_and_answers, int(session_length))
        random.shuffle(session['cards'])
        return redirect(url_for('index'))
    return render_template("Menu.html")

@app.route("/")
def index():
    if 'cards' not in session or not session['cards']:
        return redirect(url_for('menu'))
    
    # If there are no more flashcards in the session, reset the session
    if not session['cards']:
        return redirect(url_for('menu'))
    
    card = session['cards'].pop()
    session['counter'] += 1

    counter = session.get('counter')  # default to 0 if counter not in session
    total = session.get('total')  # default to 0 if total not in session
    
    return render_template("index.html", card=card, counter=counter, total=total)

if __name__ == "__main__":
    app.run(debug=True)