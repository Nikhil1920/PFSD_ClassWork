import json
f = open('States.json')
data = json.load(f)
for i in data['states']:
    print(i['name'])
f.close()
