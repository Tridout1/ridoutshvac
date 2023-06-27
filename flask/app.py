# ===== Ridouts HVAC =====
#Tyler Ridout

from flask import Flask, Response, session, request, render_template, redirect, url_for, abort, jsonify, send_file

# make sure the script's directory is in Python's import path
# this is only required when run from a different directory
import os, sys
script_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(script_dir)

app = Flask(__name__)
# app.config.from_object(app_config)
app.secret_key = app.config['SECRET_KEY']
app.debug = False


# leave this route to redirect the / route to home page

@app.get('/')
def homepage():
    return render_template("homepage.html")

    # return redirect(url_for('get_home'))

# @app.get('/home/')
# def get_home():
#     return render_template('homepage.html')