from flask import Flask, render_template, jsonify
from random import sample
import flask
from influxdb import InfluxDBClient

app = flask.Flask(__name__)
infdb = InfluxDBClient(host='localhost', port=8086)
dblist = infdb.get_list_database()

def checkInfluxdb(self):
  for element in self.dblist:
    if element.get('name',None) == 'iiot':
      self.infdb.switch_database('iiot')
      print("iiot database existes and switched...")
    else:
      print("There is no database named iiot...")

@app.route('/')
def index():
  return render_template('chart.html')
  
@app.route('/data')
def data():
  return jsonify({'results' : sample(range(1,10), 5)})


if __name__=='__main__':
  checkInfluxdb()
  app.run(host="0.0.0.0", port=int("80"), debug=True)