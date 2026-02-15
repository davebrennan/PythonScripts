import csv
import json

#name of the imported file
inputFile = 'input.csv'

# what is the file delimiter ex: comma ',' or tab '\t' or pipe '|'
delimiter2 = '|'

print("Opening up " + inputFile)

with open(inputFile, mode='r', newline='', encoding='utf-8') as csvfile:
    data = list(csv.DictReader(csvfile, delimiter = delimiter2))

print("Opened and Saved Data")

with open('output.json', mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)
    
print("json file opened and dumped")
    
