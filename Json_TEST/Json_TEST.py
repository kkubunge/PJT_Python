import json

with open('TEST.json', 'r') as json_file:
    values = json.load(json_file)

    print(values['TEST']['TEST2']['Water'])
    print(values['web']['languages'][0])
    print(len(values['TEST']['TEST2']))
    print(len(values['web']['languages']))
