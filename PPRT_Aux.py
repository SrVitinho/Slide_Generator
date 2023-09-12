from pptx.util import Inches
import math


def fix_lines(resumo):
    string_chunks = resumo.split()
    line = ""
    clean_resumos = []

    for word in string_chunks:
        if len(line + word) < 80:
            line = line + " " + word
        else:
            clean_resumos.append(line)
            line = word

    return clean_resumos


def get_sizes(resumo):
    resumo_in_lines = fix_lines(resumo)
    line_count = len(resumo_in_lines)
    if line_count <= 17:
        variable_size_top = math.ceil(line_count / 19)
    else:
        variable_size_top = 1
    top = Inches(1.5) + Inches(4) - Inches(variable_size_top * 4)
    height = Inches(2) + Inches(variable_size_top * 4)
    return top, height
