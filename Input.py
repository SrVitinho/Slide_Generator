import PyPDF2
import re
import os
import textract
import docx2txt


def pdf_text():
    path = '/home/ec2-user/input_file/word/'
    name = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            name.append(file_name)
    final_path = path + name[0].__str__()
    final_text = docx2txt.process(final_path)
    return final_text


def clean_inputs():
    path = '/home/ec2-user/input_file/word/'
    list = os.listdir(path)
    try:
        for file in list:
            remove_path = path + file
            os.remove(remove_path)
    except Exception as err:
        print(err)
    else:
        print('Folder Cleaned')