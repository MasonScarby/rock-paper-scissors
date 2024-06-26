import flask
from flask import Flask, redirect, render_template, request
import sqlalchemy 
from sqlalchemy import *


app = Flask(__name__)
conn_str = 'mysql://root:Cookiebear1@/180final'
engine = create_engine(conn_str, echo = True)
conn = engine.connect()
app.secret_key = 'secret key'


Dict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

# Home page
@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('rock_paper_scissors.html', dict= Dict)


if __name__ == '__main__':
    app.run(debug=True)
