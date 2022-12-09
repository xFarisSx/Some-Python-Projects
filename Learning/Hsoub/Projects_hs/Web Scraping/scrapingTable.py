import bs4
import requests
import csv
from pathlib import Path

res = requests.get('https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers')

soup = bs4.BeautifulSoup(res.text, 'html.parser')

table_soup = soup.find_all('table')
filteredTable = [table for table in table_soup if table.caption is not None]
# print(filteredTable)

requiredTable = None

for table in filteredTable:
    if str(table.caption.text).strip().startswith('Top first languages by population per CIA'):
        requiredTable = table
        break

# print(requiredTable)

rows = requiredTable.find_all('tr')
print(rows)
headers = [head.text.strip() for head in rows[0].find_all('th')]
print(headers)
data = []
for rowData in rows:
    value = rowData.find_all('td')
    value_text = [db.text.strip() for db in value]

    if len(value_text) == 0: continue

    data.append(value_text)

file = open('wikipedia.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(headers)
writer.writerows(data)