import csv
import json

tables = [
    'characters',
    'paragraphs',
    'chapters',
    'works'
]

d = {}

for table in tables:
    with open(f'csv/{table}.csv', 'r') as in_file:
        reader = csv.DictReader(in_file)
        d[table] = list(reader)

with open('json/normalized.json', 'w') as out_file:
    out_file.write(json.dumps(d, sort_keys=True, indent=2))
