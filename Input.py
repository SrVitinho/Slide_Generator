import PyPDF2
import re
import os
import textract
import docx2txt


def pdf_text():
    path = '/home/ec2-user/' + 'input_file/'
    name = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            name.append(file_name)
    final_path = path + name[0].__str__()
    final_text = docx2txt.process(final_path)
    return final_text
