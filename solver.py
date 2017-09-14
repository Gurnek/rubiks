'''
this file will host the algorithm for reading and solving the cube matrix
and generating the solving sequence for the cube.readsol function to use.
'''
import numpy as np

corner_alg = {
    'b' : {
        'moveset' : 'RuLuurURuurlU',
        'delta' : ((0, 0, 0), (0, 0, 2), (0, 0, 1), (0, 1, 0), (2, 0, 0), (3, 0, 0), (2, 0, 1), (3, 0, 1), (3, 0, 2), (4, 0, 2))
    },

    'c' : {
        'moveset' : 'frURUrufuFRfUff',
        'delta' : ((0, 0, 0), (0, 2, 2), (0, 1, 0), (0, 0, 1), (1, 0, 2), (3, 0, 2), (2, 0, 0), (4, 0, 0), (2, 0, 2), (3, 0, 2))
    },

    'd' : {
        'moveset' : 'ffruBfflDldll',
        'delta' : ((0, 0, 0), (0, 2, 0), (0, 1, 0), (0, 0, 1), (1, 0, 0), (2, 0, 0), (2, 0, 1), (3, 0, 1), (2, 0, 2), (3, 0, 2))
    },

    'f' : {
        'moveset' : 'FufUFulfRfrfLff',
        'delta' : ((0, 0, 0), (2, 0, 2), (0, 1, 0), (0, 0, 1), (0, 2, 0), (2, 0, 0), (1, 0, 0), (3, 0, 2), (2, 0, 1), (3, 0, 1))
    },

    'g' : {
        'moveset' : 'FruRfflDldllF',
        'delta' : ((0, 0, 1), (0, 1, 0), (0, 0, 0), (2, 2, 2), (1, 2, 0), (2, 0, 0), (2, 0, 1), (3, 0, 1), (3, 0, 2), (5, 0, 0))
    },

    'h' : {
        'moveset' : 'rDFrURfRBRbrd',
        'delta' : ((0, 0, 0), (2, 2, 0), (0, 0, 1), (0, 1, 0), (2, 0, 0), (5, 2, 0), (2, 0, 1), (3, 0, 1), (3, 0, 2), (3, 2, 2))
    },

    'i' : {
        'moveset' : 'uubUfuFBuufuF',
        'delta' : ((0, 0, 0), (1, 0, 0), (0, 0, 1), (0, 1, 0), (0, 2, 0), (3, 0, 2), (2, 0, 1), (3, 0, 1), (2, 0, 0), (2, 0, 2))
    },

    'j' : {
        'moveset' : 'uuluLuFuluLUf',
        'delta' : ((0, 1, 0), (0, 0, 1), (0, 0, 0), (1, 0, 2), (0, 2, 2), (2, 0, 0), (2, 0, 1), (3, 0, 1), (3, 0, 2), (4, 0, 0))
    },

    'k' : {
        'moveset' : 'RUrrfRBDrdFRb',
        'delta' : ((0, 0, 0), (1, 2, 2), (0, 0, 1), (0, 1, 0), (2, 0, 1), (3, 0, 1), (2, 0, 0), (4, 2, 0), (3, 0, 2), (5, 0, 2))
    },

    'l' : {
        'moveset' : 'ufUFrfURUruuFRU',
        'delta' : ((0, 0, 1), (0, 1, 0), (0, 0, 0), (1, 2, 0), (2, 0, 1), (3, 0, 1), (2, 0, 0), (5, 0, 0), (2, 2, 2), (3, 0, 2))
    }
}
edge_alg = {}
move_string = ''
def solve(matrix):
    iterator = np.nditer(matrix, flags = ['multi_index'])

    while not iterator.finished:
        value = iterator[0]
        coords = iterator.multi_index

        iterator.iternext()
