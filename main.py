import Text_Manipulation
import Input
from PowerPoint import Ppt
from llama_querys import query_llama
import AWS_operations

if __name__ == '__main__':
    Input.clean_inputs()
    AWS_operations.get_files()
    word_text_raw = Input.pdf_text()
    word_text = Text_Manipulation.clean_text(word_text_raw)
    keywords = Text_Manipulation.clean_key_phrases(word_text)
    resumos = query_llama(keywords)
    prs = Ppt("Apresentacao", resumos)
    for item in range(len(keywords)):
        prs.add_page(keywords[item][0])
    prs.save()
    AWS_operations.send_ppt()
    AWS_operations.kill_ec2()
