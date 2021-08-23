from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def index():
  items=[
  {'id':1, 'name':'Ashok', 'barcode':'1232453453','phone':'9951558825','price':500},
      {'id':2, 'name':'Amani', 'barcode':'1232453453','phone':'9951558825','price':500},
      {'id':3, 'name':'Arun', 'barcode':'1232453453','phone':'9951558825','price':500}
  ]
  return render_template('home.html',items_sec=items)
@app.route('/about')
def about_page():  
  return render_template('about.html')
