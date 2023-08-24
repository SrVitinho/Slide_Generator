from llama_cpp import Llama
from tqdm import tqdm

LLM = Llama(model_path="C:/Users/Vitor/Documents/Projects/Slide_Generator/llama_model.bin", n_ctx=1000)


def query_resumo_llm(topic):
    query = 'Faça tópicos de slide sobre ' + topic + '.'
    output = LLM(query, max_tokens=1000)
    resumo = output["choices"][0]["text"]
    return resumo


def query_llama(keys):
    resumos = []
    for phrase in tqdm(keys):
        query = 'faça um resumo sobre ' + phrase[0] + '.'
        output = LLM(query, max_tokens=1000)

        print(output["choices"][0]["text"])
        resumos.append(output["choices"][0]["text"])

    return resumos
