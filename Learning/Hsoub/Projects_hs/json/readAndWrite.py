stringOfJsonData = '{ "name": "Faris" , "isCat": true, "niceCaught": 0, "felineIQ": null}'

import json

# Read
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(type(jsonDataAsPythonValue))

# Write
pythonValue = {
    "isCat": True,
    'niceCaught':0,
    "name":'faris',
    'felineIQ': None
}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
