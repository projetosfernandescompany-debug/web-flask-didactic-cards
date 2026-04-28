import csv
from flask import Blueprint, render_template

computer_bp = Blueprint('computer-architecture', __name__)

@computer_bp.route('/arquitetura-cisc-x-risc')
def arquitetura_cisc_x_risc():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR = os.path.join(BASE_DIR, "file", "Arquitetura de Computadores")

    list_quest = []
    with open(f"{DIR}/Arquitetura CISC X RISC.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/arquitetura-cisc-x-risc.html', quest=list_quest)

@computer_bp.route('/base-computacional')
def base_computacional():
    list_quest = []
    with open("./api/file/Arquitetura de Computadores/Base Computacional.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/base-computacional.html', quest=list_quest)

@computer_bp.route('/componentes-de-hardware')
def componentes_de_hardware():
    list_quest = []
    with open("./api/file/Arquitetura de Computadores/Componentes de hardware.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/componentes-de-hardware.html', quest=list_quest)

@computer_bp.route('/logica-digital-e-algebra-booleana')
def logica_digital_e_algebra_booleana():
    list_quest = []
    with open("./api/file/Arquitetura de Computadores/Lógica Digital e Álgebra Booleana.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/logica-digital-e-algebra-booleana.html', quest=list_quest)

@computer_bp.route('/processamento-em-paralelo')
def processamento_em_paralelo():
    list_quest = []
    with open("./api/file/Arquitetura de Computadores/Processamento em Paralelo.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/processamento-em-paralelo.html', quest=list_quest)

@computer_bp.route('/representacao-de-dados')
def representacao_de_dados():
    list_quest = []
    with open("./api/file/Arquitetura de Computadores/Representação de dados.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/representacao-de-dados.html', quest=list_quest)

