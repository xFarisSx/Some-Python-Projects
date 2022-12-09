import csv
from pathlib import Path

# header = ["Name", "Salary", "Date"]
# data = [
#     ['faris', 1000, '09/09/2020'],
#     ['omar', 1000, '09/09/2020'],
#     ['emad', 1000, '09/09/2020'],
#     ['selena', 1000, '09/09/2020']
# ]
#
# file = open('csv_file.csv', 'w', newline='')
# writer = csv.writer(file)
#
# # writer.writerow(['Ahmad', 1000, '09/09/2020'])
# writer.writerow(header)
# writer.writerows(data)
# file.close()

header = ["Name", "Salary", "Date"]
data = [
    ['faris', 1000, '09/09/2020'],
    ['omar', 1000, '09/09/2020'],
    ['emad', 1000, '09/09/2020'],
    ['selena', 1000, '09/09/2020']
]

file = open('csv_file.csv', 'w', newline='')
writer = csv.writer(file, delimiter=",",lineterminator="\n")

# writer.writerow(['Ahmad', 1000, '09/09/2020'])
writer.writerow(header)
writer.writerows(data)
file.close()