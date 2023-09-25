from pptx.util import Inches
import math


def fix_lines(resumo):
    string_chunks = resumo.split()
    print('len chunks = ' + len(string_chunks).__str__())
    line = ""
    current_size = 0
    for word in string_chunks:
        if (current_size + len(word)) < 35:
            line = line + " " + word
            current_size += len(word) + 1
        else:
            line = line + "\n " + word
            current_size = 0

    return line


def get_sizes(resumo):
    line_count = resumo.count('\n')
    if line_count <= 15:
        variable_size_top = math.ceil(line_count / 17)
    else:
        variable_size_top = 1
    top = Inches(1.5) + Inches(4) - Inches(variable_size_top * 4)
    height = Inches(2) + Inches(variable_size_top * 4)
    return top, height


def get_text_pages(resumo):
    list_resumos = []
    if resumo.count('\n') >= 15:
        while resumo.count('\n') >= 15:
            line = (i for i, l in enumerate(resumo) if l == '\n')

            for x in range(15):
                next(line)
            index = next(line)
            list_resumos.append(resumo[:index])
            resumo = resumo[index:]
        list_resumos.append(resumo)
    else:
        list_resumos.append(resumo)
    print(len(list_resumos))
    print('end')
    return list_resumos