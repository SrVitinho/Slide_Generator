import yake
import spacy
import pke

nlp = spacy.load("pt_core_news_lg")


def key_extractor(text_final):
    doc = nlp(text_final)
    names = []

    for ent in doc.ents:
        if ent.label_ == "PER":
            names.append(ent)
            print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print('--------------------------')
    return ent


def clean_text(text):
    cut = text.find("Referências")
    text_final = text[:cut]
    print('------------------------------')
    return text_final


def get_keywords(text):
    custom_kw_extractor = yake.KeywordExtractor(lan="pt", top=5)
    keywords = custom_kw_extractor.extract_keywords(text)

    for kw in keywords:
        print(kw)

    print("--------------------------")
    print("--------------------------")

    # pos = {'de', 'De', 'Da', 'da', 'Do', 'do'}

    extractor = pke.unsupervised.TopicRank()

    extractor.load_document(input=text, language='pt')

    extractor.candidate_selection()

    extractor.candidate_weighting()

    keyphrases = extractor.get_n_best(n=10)

    for key in keyphrases:
        print(key)
    return keywords


def clean_key_phrases(text):
    keywords = get_keywords(text)
    drops = []
    for key in keywords:
        topic = key[0]
        word_count = len(topic.split())
        if word_count > 1:
            next
        else:
            drops.append(key)
    for drop in drops:
        keywords.remove(drop)
    print('------------------------------------------')
    return keywords
