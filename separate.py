import PyPDF2
import os

merger = PyPDF2.PdfMerger()

doc = PyPDF2.PdfReader("./pdf's/documento.pdf")

print('Para extraer un archivo se necesita una página de inicio y una página final')
pp1 = int(input(f"La página de inicio es: "))-1
pp2 = int(input(f"La página final es: "))-1
merger.append(fileobj= doc, pages= (pp1,pp2))
    

# Creamos el archivo, el parametro es el nombre del nuevo archivo.
merger.write("file-separate.pdf")
print("ARCHIVO SEPARADO CORRECTAMENTE")
    # Se cierra el archivo.
merger.close()
