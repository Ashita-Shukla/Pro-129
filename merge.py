import csv
dataset1 = []
dataset2 = []
with open("final.csv", "r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset1.append(row)

with open("main_final_sorted1.csv", "r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset2.append(row)

headers1 = dataset1[0]
headers2 = dataset2[0]

planetdata1 = dataset1[1:]
planetdata2 = dataset2[1:]

headers = headers1+ headers2
planet_data = []

for index, data_row in enumerate(planetdata1):
    planet_data.append(planetdata1[index]+planetdata2[index])

with open("merge_dataset.csv", "a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)
