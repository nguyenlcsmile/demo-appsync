import json

dataJson = open('onBoarding.json')
data = json.load(dataJson)
for i in data:
    print(i)
    break
