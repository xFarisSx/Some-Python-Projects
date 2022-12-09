import openpyxl, sys
from openpyxl.styles import Font

if len(sys.argv) == 3:
    try:
        numbery = int(sys.argv[1])
        numberx = int(sys.argv[2])

    except Exception as e:
        print(e)

    exceptFile = openpyxl.Workbook()
    sheet = exceptFile.active

    for y in range(numbery + 1):
        for x in range(numberx + 1):

            isHeader = False

            if x == 0 and y == 0:
                isHeader = True
                n = ''

            elif x == 0:
                isHeader = True
                n = y

            elif y == 0:
                isHeader = True
                n = x

            else:
                n = x * y

            cell = sheet.cell(row=x+1,column=y+1)

            if isHeader:
                cell.font = Font(bold=True)

            cell.value = n

    exceptFile.save(f'multiplaction_table_{numbery}.xlsx')

    print('Saved as','multiplaction_table_'+str(numbery)+'.xlsx')

else:
    print('Enter 2 args')