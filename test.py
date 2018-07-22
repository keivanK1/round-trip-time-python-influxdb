import sys
import json
#print(str(input("")))


#temp = json.loads([{'name': '_internal'}, {'name': 'pyexample'}])
#print(temp)

temp = [{'name': '_internal'}, {'name': 'pyexample'}]

print(temp)
for element in temp:
  if element.get('name',None) == 'pyexample':
    print("Hi")
  #print(element.get('name',None))
  # if element == "pyexample":
  #   print("Hi")