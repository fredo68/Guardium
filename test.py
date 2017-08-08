from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

canvas = canvas.Canvas("Welfare.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica',12)

canvas.drawString(30,750,'TEST')

canvas.line(480,747,580,747)

canvas.save()
