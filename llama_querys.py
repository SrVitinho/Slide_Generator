from llama_cpp import Llama
from tqdm import tqdm

LLM = Llama(model_path="/home/ec2-user/llama_model.bin", n_ctx=1000, n_gpu_layers=-1)


def query_resumo_llm(topic):
    query = 'Faça tópicos de slide sobre ' + topic + '.'
    output = LLM(query, max_tokens=1000)
    resumo = output["choices"][0]["text"]
    return resumo


def query_llama(keys):
    resumos = []
    for phrase in tqdm(keys):
        query = "O que é '" + phrase[0] + "' ?"
        output = LLM(query, max_tokens=1000)

        print(output["choices"][0]["text"])
        parcial_resumo = output["choices"][0]["text"]
        resumo = parcial_resumo[2:]
        resumos.append(resumo)

    return resumos
