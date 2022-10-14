import docx


def getText(filename):
    doc = docx.Document(Path('files', filename))
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)