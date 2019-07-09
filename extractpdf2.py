# Extract images from a PDF file and convert them to PNG file

import fitz
doc = fitz.open("webscraper.pdf")
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("images/p%s-%s.png" % (i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("images/p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None
print("Extraction and conversion complete")
