import socket
import threading
import time
import datetime
from influxdb import InfluxDBClient
import json

class Server:
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make TCP connection on IPv4
  ip = '0.0.0.0'            # in order to get the ip of server
  port = 800
  connections = []
  buffSize = 1024
  
  def __init__(self):    
    self.checkInfluxdb(self)
    self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.soc.bind((self.ip, self.port))
    self.soc.listen(1)

  def connHandle(self, conn, client):
    while True:
      data = conn.recv(self.buffSize)
      #for connection in self.connections:
      #  connection.send(bytes(data))
      rcvTime = datetime.datetime.now()
      if not data:
        self.connections.remove(conn)
        conn.close()
        break
      else:
        print((rcvTime - datetime.datetime.strptime(data.decode('utf-8'), '%Y-%m-%d %H:%M:%S.%f')).total_seconds())

  def runServer(self):
    while True:
      conn, client = self.soc.accept()
      th = threading.Thread(target=self.connHandle, args=(conn, client))
      th.daemon = True
      th.start()
      conn.send(bytes(str(datetime.datetime.now()), 'utf-8'))
      self.connections.append(conn)
      #print (self.connections)
  def checkInfluxdb(self):
    infdb = InfluxDBClient(host='localhost', port=8086)
    dblist = client.get_list_database()
    for element in dblist:
      if element.get('name',None) == 'iiot':
        client.switch_database('iiot')
        print("iiot database existes and switched...")
      else:
        client.create_database('iiot')
        client.switch_database('iiot')
        print("Influxdb with name iiot created...")

server = Server()
server.runServer()