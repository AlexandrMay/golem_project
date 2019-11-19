import jsonpath
import json

neededParameters = ['ItemsCount.Ordering', 'ItemsCount.Capturing', 'ItemsCount.Indexing', 'ItemsCount.Verification']

def deserializationOfResponse(response, parameters):
    values = []
    for i in parameters:   
        value = jsonpath.jsonpath(response.json(), i)
        values.append(value[0])
    return values

def writeToJson(orderNumber, orderNumberValue, docNumber, docNumberValue):
    to_json = {orderNumber: orderNumberValue, docNumber: docNumberValue}
    with open ('temp_file.json', 'w') as f:
        json.dump(to_json, f)

def readFromJson(key):
    with open ('temp_file.json') as f:
        content = f.read()
        temp = json.loads(content)
    return temp[key]
