import Text_Manipulation
import Input
from PowerPoint import Ppt
from Text_Manipulation import get_keywords
from Input import pdf_text
from llama_querys import query_llama

if __name__ == '__main__':
    word_text_raw = Input.pdf_text()
    word_text = Text_Manipulation.clean_text(word_text_raw)
    keywords = Text_Manipulation.clean_key_phrases(word_text)
    resumos = query_llama(keywords)
    prs = Ppt('teste1', resumos)
    prs.add_page(keywords[0][0])
    prs.add_page(keywords[1][0])
    prs.save()

