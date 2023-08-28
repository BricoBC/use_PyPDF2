import PyPDF2

password = input("Ingresa la contraseña: ")

reader = PyPDF2.PdfReader("encrypted-pdf.pdf")
writer = PyPDF2.PdfWriter()

if reader.is_encrypted:
    reader.decrypt(password)

for page in reader.pages:
    writer.add_page(page)

with open("decrypted-pdf.pdf", "wb") as f:
    writer.write(f)