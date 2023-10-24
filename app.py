from flask import Flask, render_template, session, redirect, url_for
import random
import os
from dotenv import load_dotenv
from flashcards_data import questions_and_answers

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

@app.route("/")
def index():
    if 'cards' not in session or not session['cards']:
        session['cards'] = questions_and_answers.copy() #  uses imported list
        random.shuffle(session['cards'])
    card = session['cards'].pop()
    return render_template("index.html", card=card)
    
if __name__ == "__main__":
    app.run(debug=True)