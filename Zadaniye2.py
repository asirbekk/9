import json

data = {}
data['people'] = []
data['people'].append({
    'товар': 'add',
    'магазин': 'add',
    'стой': 'Uzbekiston'
})
print(data)


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Товар: ' + p['товар'])
        print('Магазин: ' + p['магазин'])
        print('Стой: ' + p['стой'])
        print('')

