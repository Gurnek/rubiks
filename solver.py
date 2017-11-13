'''
this file will host the algorithm for reading and solving the cube matrix
and generating the solving sequence for the cube.readsol function to use.
'''

import pandas as pd
from matrix import numbering

list_of_names = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x']
preDataframe_c = {
    'moveset': pd.Series([
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
    ], index=list_of_names),

    'delta': pd.Series([
        '000 002 001 010 200 300 201 301 302 402',
        '000 022 001 010 102 302 200 400 202 302',
        '000 020 001 010 100 200 201 301 202 302',
        '000 202 001 010 020 200 100 302 201 301',
        '000 222 001 010 120 200 201 301 302 500',
        '000 220 001 010 200 520 201 301 302 322',
        '000 100 001 010 020 302 201 301 200 202',
        '000 102 010 001 022 200 201 301 302 400',
        '000 122 001 010 201 301 200 420 302 502',
        '000 120 001 010 201 301 200 500 222 302',
        '000 400 001 010 022 302 200 102 201 301',
        '000 402 001 010 002 200 201 301 300 302',
        '000 422 001 010 200 320 201 301 302 522',
        '000 420 001 010 122 302 200 502 201 301',
        '000 300 010 001 002 302 201 301 200 402',
        '000 322 010 001 200 220 201 301 302 520',
        '000 320 010 001 200 522 201 301 302 422',
        '000 500 010 001 120 302 200 222 201 301',
        '000 502 010 001 122 200 201 301 302 420',
        '000 522 010 001 200 422 201 301 302 320',
        '000 520 010 001 201 301 200 322 220 302',
    ], index=list_of_names)
}
preDataframe_e = {
    'moveset': pd.Series(),
    'delta': pd.Series()
}
corner_alg = pd.DataFrame(preDataframe_c)

edge_alg = pd.DataFrame(preDataframe_e)
move_string = ''


def dec_to_tern(num):
    """Turn decimal num to ternary."""
    num = divmod(num, 3)
    num = list(num)
    num[1] -= 1
    coords = ''
    for coord in num:
        coords += coord
    return coords


def solve(matrix):
    """Take a numpy matrix and solve it."""
    numbering(matrix)
