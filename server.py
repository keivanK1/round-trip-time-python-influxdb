import socket
import threading

class Server:
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make TCP connection on IPv4
  ip = '0.0.0.0'            # in order to get the ip of server
  port = 80
  connections = []
  buffSize = 1024
  
  def __init__(self):    
    self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.soc.bind((self.ip, self.port))
    self.soc.listen(1)

  def connHandle(self, conn, client):
    while True:
      data = conn.recv(self.buffSize)
      for connection in self.connections:
        connection.send(bytes(data))
      if not data:
        self.connections.remove(conn)
        conn.close()
        break

  def runServer(self):
    while True:
      conn, client = self.soc.accept()
      th = threading.Thread(target=self.connHandle, args=(conn, client))
      th.daemon = True
      th.start()
      self.connections.append(conn)
      print (self.connections)

server = Server()
server.runServer()