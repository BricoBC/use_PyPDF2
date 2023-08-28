#Leer un archivo con una rotación
from PyPDF2 import *

#Variable en modo lectura a un archivo
reader = PdfReader("decrypted-pdf.pdf")

#Especificamos una página
page = reader.pages[5];

#Elegimos la rotación que tiene

#print(page.extract_text((0, 90)))
#print(page.extract_text((0, 270)))
#print(page.extract_text((0, 180)))
