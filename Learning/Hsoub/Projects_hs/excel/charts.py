import openpyxl

excelFile = openpyxl.load_workbook('example.xlsx')
sheet = excelFile['Sheet1']

# Charts
title = openpyxl.chart.Reference(sheet, min_col=1, max_col=1, min_row=1, max_row=6)
data = openpyxl.chart.Reference(sheet, min_col=2, max_col=2, min_row=1, max_row=6)
chart = openpyxl.chart.LineChart()

chart.title = 'My Chart'
chart.add_data(data=data)
chart.set_categories(title)

sheet.add_chart(chart, 'E8')

excelFile.save(filename='example.xlsx')