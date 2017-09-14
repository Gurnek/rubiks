'''
this file will host the algorithm for reading and solving the cube matrix
and generating the solving sequence for the cube.readsol function to use.
'''
import numpy as np
import pandas as pd
list_of_names = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
preDataframe = {
    'moveset' : pd.Series([
        'RuLuurURuurlU',
        'frURUrufuFRfUff',
        'ffruBfflDldll',
        'FufUFulfRfrfLff',
        'FruRfflDldllF',
        'rDFrURfRBRbrd',
        'uubUfuFBuufuF',
        'uuluLuFuluLUf',
        'RUrrfRBDrdFRb',
        'ufUFrfURUruuFRU',
    ], index = list_of_names),

    'delta' : pd.Series([
        '000 002 001 010 200 300 201 301 302 402',
        '000 022 010 001 102 302 200 400 202 302',
        '000 020 010 001 100 200 201 301 202 302',
        '000 202 010 001 020 200 100 302 201 301',
        '001 010 000 222 120 200 201 301 302 500',
        '000 220 001 010 200 520 201 301 302 322',
        '000 100 001 010 020 302 201 301 200 202',
        '010 001 000 102 022 200 201 301 302 400',
        '000 122 001 010 201 301 200 420 302 502',
        '001 010 000 120 201 301 200 500 222 302'
    ], index = list_of_names)
}
corner_alg = pd.DataFrame(preDataframe)

edge_alg = {}
move_string = ''
def solve(matrix):
    iterator = np.nditer(matrix, flags = ['multi_index'])

    while not iterator.finished:
        value = iterator[0]
        coords = iterator.multi_index

        iterator.iternext()
