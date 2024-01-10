import json

# file=open('friends_json.txt','r')
# file_contents=json.load(file)
# file.close()
# print(file_contents['friends'][0])
# cars=[
#
#     {'make':'ford','model':'Fiesta'},
#     {'make':'Ford','model':'Focus'}
# ]
# file=open('car_json.txt','w')
# json.dump(cars,file)
# file.close()
# my_json_string='[{"name":"Alfa Romeo","released":1950}]'
# incorrect_car=json.loads(my_json_string)
# print(incorrect_car[0]['name'])
with open('friends_json.txt','r') as file:
     file_contents=json.load(file)
print(file_contents['friends'][0])
cars=[
 {'make':'ford','model':'Fiesta'},
  {'make':'Ford','model':'Focus'}
]

with open('friends_json.txt', 'w') as file:
    json.dump(cars,file)
