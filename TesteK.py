import PyPDF2
import re

pdf_file = open('C:/Users/kayky/Downloads/Relatório 4.pdf', "rb")
read_pdf = PyPDF2.PdfReader(pdf_file)
number_of_pages = len(read_pdf.pages)

#lê a primeira página completa
page = read_pdf.pages[0]
page_content = page.extract_text()

# faz a junção das linhas
parsed = ''.join(page_content)

print("Sem eliminar as quebras")
print(parsed)

# remove as quebras de linha
parsed = re.sub('n', '', parsed)
print("Após eliminar as quebras")
print(parsed)




