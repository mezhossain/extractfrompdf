# extractpdf1.py
# Extract text from a selected page
# from a PDF file using Python

import PyPDF2
pdfFileObj = open('bootstrap.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(1)
print(pageObj.extractText())
pdfFileObj.close()
