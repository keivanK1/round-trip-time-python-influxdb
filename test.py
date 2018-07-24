# def test():
#   return [1, 2, 3], ["a", "b", "c"]
# a, b = test()
# print(a)

# import json
# a = json.loads(json.dumps({'('latency', None)': [{'time': '2018-07-24T14:28:24.616756992Z', 'moving_average': 71.39750000000001}, {'time': '2018-07-24T14:28:27.850713088Z', 'moving_average': 128.38525}, {'time': '2018-07-24T14:28:30.940610048Z', 'moving_average': 221.55975}, {'time': '2018-07-24T14:28:33.530544896Z', 'moving_average': 220.5625}, {'time': '2018-07-24T14:28:36.638825984Z', 'moving_average': 224.987}, {'time': '2018-07-24T14:28:39.643372032Z', 'moving_average': 171.44175}]}),sort_keys=False, indent=4)
# for element in a:
#   print(element)

# from random import sample

# print(sample(range(1,10), 5))

# a = [{'time': '2018-07-23T18:01:59.27411712Z', 'client': '1', 'host': 1, 'value': 14.942}, {'time': '2018-07-23T18:02:02.274283008Z', 'client': '1', 'host': 1, 'value': 14.965}, {'time': '2018-07-23T18:02:05.280931072Z', 'client': '1', 'host': 1, 'value': 18.375}, {'time': '2018-07-23T18:02:08.281195008Z', 'client': '1', 'host': 1, 'value': 15.458}]
# b=[]
# for element in a:
#   b.append(element['value'])
# print(b)
# print(a[0]['time'])

#####################################Moving average in influxdb
# print(client.query('SELECT moving_average("value",4) FROM "iiot"."autogen"."latency"'))