# Library Imports
from cs50 import SQL
from flask import Flask, render_template


# Application Configuration
app = Flask(__name__, static_folder='static')


# Define SQLite Database
db = SQL('sqlite:///homunculus.db')


# Application Homepage
@app.route('/')
def index():

    return render_template('index.html')


# Check Current Script for Main or Module
if __name__ == '__main__':
    app.run(debug=True)