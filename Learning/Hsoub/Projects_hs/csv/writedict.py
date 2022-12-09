import csv
from pathlib import Path

with open('csv_file.csv', 'w') as f:
    dictWriter = csv.DictWriter(f, ['Name', 'Salary', 'Date'])
    dictWriter.writeheader()
    dictWriter.writerow({'Name' : 'Faris', 'Salary':1500, 'Date': '06/06/2033'})
