import Text_Manipulation
import Input
from PowerPoint import Ppt
from Text_Manipulation import get_keywords
from Input import pdf_text
from llama_querys import query_llama
import AWS_operations

if __name__ == '__main__':
    AWS_operations.get_wordx()
    word_text_raw = Input.pdf_text()
    word_text = Text_Manipulation.clean_text(word_text_raw)
    keywords = Text_Manipulation.clean_key_phrases(word_text)
    resumos = query_llama(keywords)
    prs = Ppt('teste1', resumos)
    for item in range(keywords):
        prs.add_page(keywords[item][0])
    prs.save()
    AWS_operations.clean_bucket()
    AWS_operations.kill_ec2()
