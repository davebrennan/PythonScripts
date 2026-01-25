import csv
import json

#name of the imported file
inputFile = 'input.csv'

# what is the file delimiter ex: comma ',' or tab '\t' or pipe '|'
delimiter = '|'

with open(inputFile, mode='r', newline='', encoding='utf-8') as csvfile:
    data = list(csv.DictReader(csvfile, delimiter = delimiter))

with open('output.json', mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)
