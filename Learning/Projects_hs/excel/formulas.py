import openpyxl

excelFile = openpyxl.load_workbook('example.xlsx')
sheet = excelFile['Sheet1']

# sheet['B7'] = '=SUM(B1:B6)'
# sheet['B7'] = '=average(B1:B6)'
# sheet['B7'] = '=COUNTIF(B1:B6, ">750")'

excelFile.save(filename='example.xlsx')