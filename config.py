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
JOIN_CLASSES = False
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
