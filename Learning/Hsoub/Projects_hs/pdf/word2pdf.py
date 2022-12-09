from docx2pdf import convert
from pathlib import Path

docx_file = Path('..', 'word', 'pdf_test_converted.docx')
pdf_file = "academy_1_converted.pdf"

multi_file = 'word_files/'

# convert(docx_file, pdf_file)
# convert(multi_file)