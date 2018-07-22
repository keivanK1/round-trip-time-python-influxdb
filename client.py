import socket
import threading
import sys
import datetime

class Client:
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make TCP connection on IPv4
  port = 800
  buffSize = 1024
  
  def __init__(self, ip):
    self.ip = ip
    self.soc.connect((self.ip, self.port))
    #sendTh = threading.Thread(target=self.sendMessage)
    #sendTh.daemon = True
    #sendTh.start()

    while True:
      data = self.soc.recv(self.buffSize)
      #rcvTime = datetime.datetime.now()
      if not data:
        break
      self.soc.send(bytes(data))
      ##print(datetime.datetime.strptime(data.decode('utf-8'), '%Y-%m-%d %H:%M:%S.%f'))
      #print((rcvTime - datetime.datetime.strptime(data.decode('utf-8'), '%Y-%m-%d %H:%M:%S.%f')).total_seconds())

  def sendMessage(self):
    while True:
      
      msg = input("")
      # tes = datetime.datetime.now().time()
      # print(tes)
      #self.soc.send(bytes(input(""), 'utf-8'))
      self.soc.send(bytes(str(datetime.datetime.now()), 'utf-8'))
      #self.soc.send(bytes(str(datetime.datetime.now().time()) + " ;;" + input(""), 'utf-8'))

if(len(sys.argv) > 1):
  client = Client(sys.argv[1])
else:
  print("Please provide the IP of server!")