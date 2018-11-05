#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
config.py

Created on Sun Oct 21 18:19:07 2018

@author: fernandotal

This flie crries the constants for universal use in the program
"""

import pandas as pd
import numpy as np
import sys as os

BASE_FOLDER = './exams'
PADRONIZED_FOLDER = './padronized'
RESULTS_FOLDER = './results'
PERCENTILE = 0.27
CONSIDERATED_TRY = 'both'  # input 'first' or 'last' or 'both'
JOIN_CLASSES = True
USELESS_INFO_USP = [
        'Sobrenome',
        'Nome',
        'Endereço de email',
        'Número USP',
        'Estado',
        'Iniciado em',
        'Completo',
        'Tempo utilizado'
        ]
IDENTIFIER_USP = ['Número USP']
USELESS_INFO_MACK = [
        'Sobrenome',
        'Nome',
        'Instituição',
        'Departamento',
        'Endereço de email',
        'Estado',
        'Iniciado em',
        'Completo',
        'Tempo utilizado'
        ]
IDENTIFIER_MACK = ['Endereço de email']
JOIN_ACTIVITIES =[
        'Atividade Virtual 1-first',
        'Atividade Virtual 1-last',
        'Atividade Virtual 2-first',
        'Atividade Virtual 2-last',
        'Atividade Virtual 3-first',
        'Atividade Virtual 3-last',
        'Atividade Virtual 4-first',
        'Atividade Virtual 4-last',
        'Atividade Virtual 5-first',
        'Atividade Virtual 5-last',
        'Atividade Virtual 6-first',
        'Atividade Virtual 6-last',
        'Atividade Virtual 7-first',
        'Atividade Virtual 7-last'
        ]