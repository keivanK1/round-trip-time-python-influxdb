from influxdb import InfluxDBClient



client = InfluxDBClient(host='0.0.0.0', port=8086)
client.create_database('iiot')

print(client)


####################################################### Drop database
# from influxdb import InfluxDBClient

# client = InfluxDBClient(host='localhost', port=8086)

# print(client.get_list_database())
# client.drop_database(str(input("")))

# print(client.get_list_database())
####################################################################