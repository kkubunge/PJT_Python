import json
from datetime import datetime

file_path = 'Json\\TEST.json'

with open(file_path, 'r') as json_file:
    values = json.load(json_file)

newData = {
    "produntID": "55555",
    "productName": "18.016",
    "imgSavePath": "H2O",
    "url":"https:\\www.naver.com",
    "imgCnt": 4,
    "downLoadDate": "1293178"
}

print(json.dumps(values, indent=4) )
print("-----------------------------------------------------------")
values['dataBackUp'].append(newData)
print(json.dumps(values, indent=4) )
print("-----------------------------------------------------------")

with open(file_path, 'w', encoding='utf-8') as outfile:
    json.dump(values, outfile, indent=4, ensure_ascii=False)


