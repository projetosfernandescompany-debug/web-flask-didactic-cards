import csv
from flask import Blueprint, render_template
from utils.slugify import data_card_computer_architecture

card_bp = Blueprint('card', __name__)

@card_bp.route('/arquitetura-de-computadores')
def arquitetura_de_computadores():
    dados = data_card_computer_architecture()
    return render_template('card/arquitetura-de-computadores.html', pages=dados)

@card_bp.route('/componentes-de-hardware')
def componentes_de_hardware():
    list_quest = []
    with open("./api/file/Componentes de hardware.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('card/componentes-de-hardware.html', quest=list_quest)

@card_bp.route('/computacao-em-nuvem')
def computacao_em_nuvem():
    list_quest = []
    with open("./api/file/Computação em Nuvem.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('card/computacao-em-nuvem.html', quest=list_quest)

@card_bp.route('/fundamentos-de-redes-de-computadores')
def fundamentos_de_redes_de_computadores():
    list_quest = []
    with open("./api/file/Fundamentos de Redes de Computadores.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('card/fundamentos-de-redes-de-computadores.html', quest=list_quest)

@card_bp.route('/introducao-a-programacao-de-computadores-com-c')
def introducao_a_programacao_de_computadores_com_c():
    list_quest = []
    with open("./api/file/Introdução à Programação de Computadores com C.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('card/introducao-a-programacao-de-computadores-com-c.html', quest=list_quest)

@card_bp.route('/introducao-a-seguranca-da-informacao')
def introducao_a_seguranca_da_informacao():
    list_quest = []
    with open("./api/file/Introdução à Segurança da Informação.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('card/introducao-a-seguranca-da-informacao.html', quest=list_quest)

@card_bp.route('/pensamento-computacional')
def pensamento_computacional():
    list_quest = []
    with open("./api/file/Pensamento Computacional.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('card/pensamento-computacional.html', quest=list_quest)