from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dynamic.html')

@app.route('/response', methods=['POST'])
def res():
    name = request.form.get("name")
    return render_template('dynamic.html', name=name)

@app.route('/list')
def list():
    names = ["bob","tom","jerry"]
    return render_template('list.html', names=names)
