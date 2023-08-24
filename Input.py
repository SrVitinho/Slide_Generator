import PyPDF2
import re
import os
import textract
import docx2txt


def pdf_text():
    path_raw = os.path.abspath(os.getcwd())
    path = path_raw + '/file/'
    name = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            name.append(file_name)
    final_path = path + name[0].__str__()
    final_text = docx2txt.process(final_path)
    # print(final_text)
    return final_text
