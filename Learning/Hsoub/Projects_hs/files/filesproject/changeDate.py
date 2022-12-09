import os, shutil, re

datePattern = "^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$"

for name in os.listdir('files'):
    search = re.search(datePattern,name)

    if search == None:
        continue

    beforePart = search.group(1)
    monthPart = search.group(2)
    dayPart = search.group(4)
    yearPart = search.group(6)
    afterPart = search.group(8)

    newfilename = beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
    print(f'Renaming {name} to {newfilename}')

    oldname = f'files/{name}'
    newname = f'files/{newfilename}'
    shutil.move(oldname,newname)