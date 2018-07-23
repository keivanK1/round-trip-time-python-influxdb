from flask import Flask, render_template, jsonify
from random import sample
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
  return render_template('chart.html')
  
@app.route('/data')
def data():
  return jsonify({'results' : sample(range(1,10), 5)})


if __name__=='__main__':
  app.run(host="0.0.0.0", port=int("80"), debug=True)
