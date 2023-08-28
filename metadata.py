#File #1
#Importamos la libreria con la cual trabajaremos
import PyPDF2

#Cargamos el archivo
doc = PyPDF2.PdfReader("./documento.pdf")

# Una variable tendrá todos los metadatos del documento
meta = doc.metadata

#Se imprime los valores de los metadato

print(type(meta))
print(meta)

#Los metadatos están compuesto por:
print(meta.author)
print(meta.creator)
print(meta.producer)
print(meta.subject)
print(meta.title)
