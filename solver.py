'''
this file will host the algorithm for reading and solving the cube matrix
and generating the solving sequence for the cube.readsol function to use.
'''
import numpy as np
import pandas as pd
list_of_names = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x' ]
preDataframe_c = {
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
        'uulUFufuLuFuf',
        'uuLuRUrluuRUr',
        'udfLulFlblBLDLU',
        'rURUrufuFRfUF',
        'ufRFrfflfLfUruR',
        'fdflFLFrFUfRD',
        'rURfRBRbrdrDF',
        'ufUFulfRfrfLf',
        'ufRflfLfruFUf',
        'UrrfRBDrdFRbR',
        'uulUfRfrffUfuFL',
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
        '001 010 000 120 201 301 200 500 222 302',
        '001 010 000 400 022 302 200 102 201 301',
        '001 010 000 402 002 200 201 301 300 302',
        '001 010 000 422 200 320 201 301 302 522',
        '001 010 000 420 122 302 200 502 201 301',
        '010 001 000 300 002 302 201 301 200 402',
        '010 001 000 322 200 220 201 301 302 520',
        '010 001 000 320 200 522 201 301 302 422',
        '010 001 000 500 120 302 200 222 201 301',
        '010 001 000 502 122 200 201 301 302 420',
        '010 001 000 522 200 422 201 301 302 320',
        '010 001 000 520 201 301 200 322 220 302',
    ], index = list_of_names)
}
preDataframe_e = {
    'moveset' : pd.Series(),
    'delta' : pd.Series()
}
corner_alg = pd.DataFrame(preDataframe_c)

edge_alg = pd.DataFrame(preDataframe_e)
move_string = ''
def solve(matrix):
    iterator = np.nditer(matrix, flags = ['multi_index'])

    while not iterator.finished:
        value = iterator[0]
        coords = iterator.multi_index

        iterator.iternext()
