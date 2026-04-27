import os
import unicodedata
import re


def slugify(text):
    text = text.strip()

    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')

    text = text.lower()

    text = re.sub(r'[^a-z0-9]+', '-', text)

    text = text.strip('-')

    return text

conteudo = os.listdir("./api/file/Arquitetura de Computadores")
def ht():
    with open("./api/templates/in.html", "r") as file:
        fil = file.read()
    for x in conteudo:
        base = x.replace(".csv", "")
        name = slugify(base)
        with open(f"./api/templates/arquitetura-de-computadores/{name}.html", "w") as f:
            f.write(fil)
            
            
def func():
    with open(f"./func.txt", "a", encoding="utf-8") as f:
        for x in conteudo:
            base = x.replace(".csv", "")
            n = slugify(base)
                
            #name = n.replace(".csv", "").replace(" ", "-").lower()
            f.write(f"""@computer_bp.route('/{n}')
def {n.replace("-", "_")}():
    list_quest = []
    with open("./api/file/Arquitetura de Computadores/{x}", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/{n}.html', quest=list_quest)""" + "\n\n")

def func1():
    content = os.listdir("./api/templates/read")
    with open(f"./func.txt", "a", encoding="utf-8") as f:
        for x in content:
            base = x.replace(".html", "-pdf")
            n = slugify(base)
                
            #name = n.replace(".csv", "").replace(" ", "-").lower()
            f.write(f"""@read_bp.route('/{n}')
def {n.replace("-", "_")}():
    return render_template('read/{n}.html', quest=list_quest)""" + "\n\n")
            
func1()