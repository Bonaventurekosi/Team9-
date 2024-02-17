# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
# import model
# import requests


# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')                  
@app.route('/index')
def index():
      return render_template("index.html")


app.route('/',methods=['POST'])
def getvalue():
    name= request.form{}
app.run(host='0.0.0.0',      port=81, debug=True)
