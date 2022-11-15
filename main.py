

import os
from datetime import date
from reportlab.pdfgen.canvas import Canvas

path = '/Users/shayankoohi/Desktop/ReceiptScreenshots/Images/'
receipts = os.listdir(path)
pageNumber = 1
for i in range(0, len(receipts), 4):
    canvas = Canvas(f"/Users/shayankoohi/Desktop/ReceiptScreenshots/Output/{date.today()}-page-{pageNumber}.pdf")
    try:
        canvas.drawImage(path + receipts[i], 0, 0, canvas._pagesize[0] / 2, canvas._pagesize[1] / 2)
        canvas.drawImage(path + receipts[i + 1], canvas._pagesize[0] / 2, 0, canvas._pagesize[0] / 2,
                         canvas._pagesize[1] / 2)
        canvas.drawImage(path + receipts[i + 2], 0, canvas._pagesize[1] / 2, canvas._pagesize[0] / 2,
                         canvas._pagesize[1] / 2)
        canvas.drawImage(path + receipts[i + 3], canvas._pagesize[0] / 2, canvas._pagesize[1] / 2,
                         canvas._pagesize[0] / 2, canvas._pagesize[1] / 2)
        canvas.save()
        pageNumber += 1
    except IndexError:
        canvas.save()
