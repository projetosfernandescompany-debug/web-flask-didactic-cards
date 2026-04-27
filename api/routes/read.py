import csv
import os
from flask import Blueprint, render_template

read_bp = Blueprint('read', __name__)

@read_bp.route('/anatomia-da-computacao-pdf')
def anatomia_da_computacao_pdf():
    return render_template('read/anatomia-da-computacao.html')

@read_bp.route('/digital-data-pdf')
def digital_data_pdf():
    return render_template('read/digital-data.html')

