from flask import Flask,render_template
import requests
import json


app = Flask(__name__)
@app.route('/')
def hello():
    req = requests.get('https://coronavirus-19-api.herokuapp.com/countries/')
    covid_Data = json.loads(req.content)
    return render_template('index.html', data=covid_Data)

app.run(debug=True)