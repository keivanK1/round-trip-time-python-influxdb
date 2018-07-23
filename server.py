import socket
import threading
import time
import datetime
from influxdb import InfluxDBClient
import json
#from http.server import BaseHTTPRequestHandler, HTTPServer

class Server:
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make TCP connection on IPv4
  ip = '0.0.0.0'            # in order to get the ip of server
  port = 800
  connections = []
  buffSize = 1024

  def __init__(self):
    self.infdb = InfluxDBClient(host='localhost', port=8086)
    self.dblist = self.infdb.get_list_database()
    self.checkInfluxdb()
    self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.soc.bind((self.ip, self.port))
    self.soc.listen(1)
    self.sendTime = datetime.datetime.now()
    
  def connHandle(self, conn, client):
    while True:
      data = conn.recv(self.buffSize)
      #for connection in self.connections:
      #  connection.send(bytes(data))
      tempTime = datetime.datetime.now()
      if not data:
        self.connections.remove(conn)
        conn.close()
        break
      else:
        index = self.connections.index(conn)
        #print((tempTime - datetime.datetime.strptime(data.decode('utf-8'), '%Y-%m-%d %H:%M:%S.%f')).total_seconds())
        latency = (tempTime - self.sendTime).total_seconds() * 1000
        print(index , " : " , latency)
        json_body = [
          {
              "measurement": "latency",
              "tags": {
                  "host": "aws"
              },
              "time": datetime.datetime.now(),
              "fields": {
                  "value": latency,
                  "client": index
              }
          }
        ]
        self.infdb.write_points(json_body)
        self.rcvTime = tempTime

  def checkLatency(self):
    while True:
      time.sleep(3)
      for conn in self.connections:
        self.sendTime = datetime.datetime.now()
        conn.send(bytes(str('a'), 'utf-8'))
        #conn.send(bytes(str(datetime.datetime.now()), 'utf-8'))
      
  def runServer(self):
    thLatency = threading.Thread(target=self.checkLatency)
    thLatency.daemon = True
    thLatency.start()
    while True:
      conn, client = self.soc.accept()
      th = threading.Thread(target=self.connHandle, args=(conn, client))
      th.daemon = True
      th.start()
      #conn.send(bytes(str(datetime.datetime.now()), 'utf-8'))
      self.connections.append(conn)
      #print (self.connections)

  def checkInfluxdb(self):
    for element in self.dblist:
      if element.get('name',None) == 'iiot':
        self.infdb.drop_database('iiot')
        print("Old database droped...")
        self.infdb.create_database('iiot')
        self.infdb.switch_database('iiot')
        return print("Old database droped, new database created and switched...")
    self.infdb.create_database('iiot')
    self.infdb.switch_database('iiot')
    return print("New database created and switched...")
      
      # else:
      #   self.infdb.create_database('iiot')
      #   self.infdb.switch_database('iiot')
      #   print("Influxdb with name iiot created...")

# class httpServer(BaseHTTPRequestHandler):

#   # GET Method
#   def do_GET(self):
#     self.send_response(200)
#     self.send_header('Content-type','text/html')
#     self.end_headers()
#     message = "Hello world!"
#     # Write content as utf-8 data
#     self.wfile.write(bytes(message, "utf8"))
#     return

# def httpRun():
#   serverIPPort = ('0.0.0.0', 8081)
#   httpd = HTTPServer(serverIPPort, httpServer)
#   print('HTTP running server...')
#   httpd.serve_forever()
  
def initialServer():
  # print('starting HTTP Server...')
  # thHTTP = threading.Thread(target=httpRun)
  # thHTTP.daemon = True
  # thHTTP.start()
  
  print('starting TCP Server...')
  server = Server()
  server.runServer()

initialServer()