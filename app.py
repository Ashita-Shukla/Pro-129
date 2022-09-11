import csv 
data = []
with open("main.csv", "r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)
headers = data[0]
planet_data = data[1:]

for data_point in planet_data:
    data_point[2] = data_point[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("main_sorted.csv", "a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)

with open('main_sorted.csv')as input, open('main_final_sorted1.csv', 'w', newline = '')as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip()for field in row):
            writer.writerow(row)

