from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def index():
  items=[
  {'id':1, 'name':'Ashok', 'phone':'9951558825','email':'pashok8825@gmail.com','dob':'24-Mar-1993'},
      {'id':2, 'name':'Amani', 'phone':'9951554425','email':'amani.palla18@gmail.com','dob':'24-Mar-1993'},
      {'id':3, 'name':'Arun', 'phone':'9951338825','email':'arunkumar5@gmail.com','dob':'24-Mar-1993'}
  ]
  return render_template('home.html',items_sec=items)
@app.route('/about')
def about_page():  
  return render_template('user_detail.html')
