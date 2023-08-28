import PyPDF2

password = input("Ingresa una contraseña: ")

doc = PyPDF2.PdfReader("./pdf's/documento.pdf")
#Variable que tiene las propiedades de escritura en un pdf
writer = PyPDF2.PdfWriter()

# Se añade todo el documento a la acción de escritura
for page in doc.pages:
    writer.add_page(page)

# Se agrega la contraseña al archivo
writer.encrypt(password)

# Se guarda el nuevo archivo a un archivo
with open("encrypted-pdf.pdf", "wb") as f:
    writer.write(f)

print("ARCHIVO ENCRIPTADO CORRECTAMENTE")