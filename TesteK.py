import PyPDF2
import re
import os

def pdf_text():
    path_raw = os.path.abspath(os.getcwd())
    path = path_raw + '/file/'
    name = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            name.append(file_name)
    final_path = path + name[0].__str__()
    pdf_file = open(final_path, "rb")
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




