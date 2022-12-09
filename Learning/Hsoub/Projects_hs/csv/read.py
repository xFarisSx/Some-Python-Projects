import csv
from pathlib import Path

file = open("csv_file.csv")
reader = csv.reader(file)

# data = list(reader)
# print(data)

for row in reader:
    print("Row #" + str(reader.line_num) + ' ' + " ".join(row))
