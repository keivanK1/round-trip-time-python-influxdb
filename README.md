# Round Trip time measurement using Python 3
This project measure the Round Trip Time (RTT) of a byte send to the client which is based on Python 3. The following picture shows what
RTT is.

![RTT](https://www.globaldots.com/wordpress/wp-content/uploads/2013/10/rtt_wikimedia.png)

There are 2 servers running namely TCP server and Flask server. TCP server will send a byte to the client, timestamp it and waits to get it back from client
and timestamp it again. The difference between these two timestamps would be the round trip time. This value would be saved on influxdb and Flask server can access it and show them on graphs.
The graphs will be updated every 3 seconds.

## Requirements

* Python 3
* Influxdb
* Flask

All of these requirements should be installed on your server but just Python 3 is needed for client. Server can be EC2 or any other provider.

## Getting Started

* Clone the repository in server and clinet:

      git clone https://github.com/keivanK1/measure-round-trip-time-Influxdb.git
      
* Run server.py on server side:

      sudo python3 server.py
      
* Run client.py on client side:

      sudo python3 client.py [Public IP of your server]
    
* Type the public IP of the server in your browser and see the RTT values.

Note that just the first 2 client will be shown on UI but you can access the RTT values of other clients through terminal of server.
