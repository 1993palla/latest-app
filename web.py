from flask import Flask, render_templete
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('home.html')
