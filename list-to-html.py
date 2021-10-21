from flask import Flask
app = Flask(__name__)

table = []
row = ["coke",1.5]
table.append(row)
row2 = ["pepsi",0.8]
table.append(row2)
row3 = ["7up",1.2]
table.append(row3)
s = sorted(table,key=lambda t:t[1])

import pandas as pd

c = ['Product', 'Price']
df = pd.DataFrame(s, columns=c)
html = df.to_html(index=False)

@app.route("/")
def hello_world():
    return html
