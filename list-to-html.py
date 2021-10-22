from flask import Flask
app = Flask(__name__)

table = []
row = ["Coke",1.5]
table.append(row)
row2 = ["Pepsi",0.8]
table.append(row2)
row3 = ["7UP",1.2]
table.append(row3)
s = sorted(table,key=lambda t:t[1])

import pandas as pd

col = ['Product', 'Price']
df = pd.DataFrame(s, columns=col)
html = '<html><head><link rel="stylesheet" href="/static/mystyle.css"></head><body>'
html += df.to_html(index=False)

@app.route("/")
def hello_world():
    return html
