import json

with open(input()) as tests_read, open(input()) as values_read:
    test = json.load(tests_read)['tests']
    values = json.load(values_read)['values']

def search(obj, key, val, key2, val2):
    """Рекурсивный поиск и замена значений"""
    for i in obj:
        if i[key] == val:
            i[key2] = val2
        elif i == list:
            for item in i[key]:
                for elem in item:
                    search(elem, key, val, key2, val2)
        elif 'values' in i:
            search(i['values'], key, val, key2, val2)

search(test, 'id', 5322, 'value', 'ура')

tests = dict()
tests['tests'] = test

for item in values:
    id = item['id']
    value = item['value']
    search(test, 'id', id, 'value', value)

with open('report.json', 'w') as file:
    json.dump(tests, file)