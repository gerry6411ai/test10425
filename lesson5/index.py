from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
    

@app.route("/user")
def user():
    return "<h1>Hello, world!</h1><p>這是我的第2頁</p>"