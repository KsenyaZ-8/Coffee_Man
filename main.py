import json

with open('coffee_houses.json', 'r', encoding='CP1251') as my_file:
    coffee_houses_data_json  = my_file.read()
coffee_houses = json.loads(coffee_houses_data_json)

for i,item in enumerate(coffee_houses):
    print(coffee_houses[i] ['Name'], *(coffee_houses[i]['geoData'] ['coordinates']),sep='\n')
my_file.close()
