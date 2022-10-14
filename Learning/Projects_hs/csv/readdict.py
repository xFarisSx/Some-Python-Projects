import csv
from pathlib import Path

with open('csv_file.csv', 'r') as f:
    dictReader = csv.DictReader(f)

    for row in dictReader:
        print(row['Name'], row['Salary'], row['Date'])