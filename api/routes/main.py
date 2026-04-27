import csv
import os
from flask import Blueprint, render_template
from utils.slugify import data_card, data_read

main_bp = Blueprint('home', __name__)

@main_bp.route('/')
@main_bp.route('/home/')
def home():
    return render_template('home/home.html')


@main_bp.route('/cards/')
def cards():
    dados = data_card()

    return render_template('home/cards.html', pages=dados)

@main_bp.route('/read/')
def read():
    dados = data_read()
    return render_template('home/read.html', pages=dados)