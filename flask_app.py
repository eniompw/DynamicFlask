from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dynamic.html')

@app.route('/response', methods=['POST'])
def hello():
    name = request.form.get("name")
    return render_template('dynamic.html', name=name)
