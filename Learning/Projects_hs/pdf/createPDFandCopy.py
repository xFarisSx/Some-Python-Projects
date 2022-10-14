from PyPDF2 import PdfFileWriter as w
from pathlib import Path
import PyPDF2

# create
pdf = w()
file = open(Path('pdf_file.pdf'), 'wb')
for i in range(5):
    pdf.addBlankPage(219,297) # size

pdf.write(file)

# copy
pdfFile = open(Path('pdf_test.pdf'), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdf.addPage(pageObj)

pdf.write(file)

file.close()