import csv, os
from pathlib import Path

for csvFilename in os.listdir(Path.home() / Path('Desktop','Programming','Python','Learning','Projects_hs','csv','Files')):
    if not  csvFilename.endswith('.csv'):
        continue

    print('Removing the header from', csvFilename, '...')
    csvRows = []
    csvFileObj = open(Path.home() / Path('Desktop','Programming','Python','Learning','Projects_hs','csv','Files', csvFilename))
    reader = csv.reader(csvFileObj)

    for row in reader:
        if reader.line_num == 1:
            continue

        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(Path.home() / Path('Desktop','Programming','Python','Learning','Projects_hs','csv','Files', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()