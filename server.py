from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/process')
def process():
  return render_template("process.html")
app.run(debug=True)
