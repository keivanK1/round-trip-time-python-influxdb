from flask import Flask, render_template, jsonify
from random import sample
import flask
from influxdb import InfluxDBClient

app = flask.Flask(__name__)
infdb = InfluxDBClient(host='localhost', port=8086)
dblist = infdb.get_list_database()
checkdb = False

def checkInfluxdb(): 
  for element in dblist:
    if element.get('name',None) == 'iiot':
      infdb.switch_database('iiot')
      print("iiot database existes and switched...")
      return True
  print("There is no database...")

# def getLatency(clientId):
#   client.query('SELECT "value" FROM "iiot"."autogen"."latency"')

@app.route('/')
def index():
  return render_template('chart.html')
  
@app.route('/data')
def data():
  if(checkdb):
    print(infdb.query('SELECT "value" FROM "iiot"."autogen"."latency"'))
  return jsonify({'results' : sample(range(1,10), 5)})



if __name__=='__main__':
  checkdb = checkInfluxdb()
  app.run(host="0.0.0.0", port=int("80"), debug=True)


# from influxdb import InfluxDBClient
# client = InfluxDBClient(host='localhost', port=8086)
# client.switch_database('iiot')
# print(client.query('SELECT "value" FROM "iiot"."autogen"."latency"'))