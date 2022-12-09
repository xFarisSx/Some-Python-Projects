import PyPDF2
from pathlib import Path

pdfFileObj = open(Path('pdf_test.pdf'), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# page number
print(pdfReader.numPages)

# read
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())


pdfFileObj.close()