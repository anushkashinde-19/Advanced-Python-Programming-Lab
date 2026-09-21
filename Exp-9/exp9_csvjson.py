import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    csvFile = open(csvFilePath, encoding="utf-8")
    csvReader = csv.DictReader(csvFile)

    for row in csvReader:
        jsonArray.append(row)

    csvFile.close()

    jsonFile = open(jsonFilePath, "w", encoding="utf-8")

    jsonString = json.dumps(jsonArray, indent=4)
    jsonFile.write(jsonString)

    jsonFile.close()


csvFilePath = "input.csv"
jsonFilePath = "output.json"

csv_to_json(csvFilePath, jsonFilePath)