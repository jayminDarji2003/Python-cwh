from PyPDF2 import PdfWriter
import os

pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]
print(pdf_files)
 
merger = PdfWriter()

for pdf in pdf_files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
