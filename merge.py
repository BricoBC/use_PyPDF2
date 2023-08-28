import PyPDF2
import os

merger = PyPDF2.PdfMerger()

files = os.listdir("./pdf's/")
print(files)

for file in files:
    doc = PyPDF2.PdfReader("./pdf's/" + file)
    merger.append(doc)

merger.write("merged.pdf")
merger.close()
