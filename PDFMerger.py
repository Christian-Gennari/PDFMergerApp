import PyPDF2
import tkinter
from tkinter import filedialog as fd	

# Hides Tkinter root window
tkinter.Tk().withdraw()

filename = fd.askopenfilenames(initialdir = "/",title = "Select files",filetypes = (("PDF files","*.pdf"),("all files","*.*"))) # show an "Open" dialog box and return the path to the selected file
filename = list(filename)
print(filename)
pdfOutputFile = fd.asksaveasfile(mode='wb', defaultextension=".pdf")

pdfWriter = PyPDF2.PdfFileWriter()

for x in filename:
	pdfFiles = open(x, "rb")
	pdfReader = PyPDF2.PdfFileReader(pdfFiles)
	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)
		pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()


#pdfOutputFile = open("combinedpdf.pdf", "wb")
#pdfWriter.write(pdfOutputFile)
#pdfOutputFile.close()
#pdf1File.close()
#pdf2File.close()

