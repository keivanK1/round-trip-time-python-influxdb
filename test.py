from flask import Flask, render_template, jsonify
from random import sample
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
  return render_template('chart.html')
  
@app.route('/data')
def data():
  #return jsonify({'results' : sample(range(1,10), 5)})
  return jsonify({'results' : queryLatency()})

a = [{'time': '2018-07-23T18:01:59.27411712Z', 'client': '1', 'host': 1, 'value': 14.942}, {'time': '2018-07-23T18:02:02.274283008Z', 'client': '1', 'host': 1, 'value': 14.965}, {'time': '2018-07-23T18:02:05.280931072Z', 'client': '1', 'host': 1, 'value': 18.375}, {'time': '2018-07-23T18:02:08.281195008Z', 'client': '1', 'host': 1, 'value': 15.458}]



def queryLatency():
  b=[]
  for element in a:
    b.append(element['value'])
  return b

if __name__=='__main__':
  app.run(host="0.0.0.0", port=int("80"), debug=True)

# from random import sample

# print(sample(range(1,10), 5))

# a = [{'time': '2018-07-23T18:01:59.27411712Z', 'client': '1', 'host': 1, 'value': 14.942}, {'time': '2018-07-23T18:02:02.274283008Z', 'client': '1', 'host': 1, 'value': 14.965}, {'time': '2018-07-23T18:02:05.280931072Z', 'client': '1', 'host': 1, 'value': 18.375}, {'time': '2018-07-23T18:02:08.281195008Z', 'client': '1', 'host': 1, 'value': 15.458}]
# b=[]
# for element in a:
#   b.append(element['value'])
# print(b)
# print(a[0]['time'])