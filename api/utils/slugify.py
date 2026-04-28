import unicodedata
import re
import os


def slugify(text):
    text = text.strip()

    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')

    text = text.lower()

    text = re.sub(r'[^a-z0-9]+', '-', text)

    text = text.strip('-')

    return text

def data_card():
    conteudo = os.listdir("../api/file")
    
    dados = []

    for x in conteudo:
        base = x.strip().replace(".csv", "")
        url = slugify(base)
        
        dados.append({
            "nome": base,
            "url_p": f"card/{url}"
        })
    
    return dados

def data_card_computer_architecture():
    conteudo = os.listdir("api/file/Arquitetura de Computadores")
    
    dados = []

    for x in conteudo:
        base = x.strip().replace(".csv", "")
        url = slugify(base)
        print(base)
        dados.append({
            "nome": base,
            "url_p": f"computer-architecture/{url}"
        })
    
    return dados

def data_read():
    dados = [
        {
            "nome": "Anatomia da Computação",
            "url_p": "read/anatomia-da-computacao-pdf"
        },
        {
            "nome": "Digital Data",
            "url_p": "read/digital-data-pdf"
        }
    ]
    
    return dados
