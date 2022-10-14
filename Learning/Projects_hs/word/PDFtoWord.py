from pdf2docx import Converter
from pathlib import Path

pdf_file = "../pdf/article/article.pdf"
docx_file = "./pdf_test_converted.docx"

# convert
cv = Converter(pdf_file)
# cv.convert(docx_file)
cv.convert(docx_file, start=1, end=5)
cv.close()
