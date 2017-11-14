"""
This will be for analyzing the preliminary array and assigning the pieces their place numbers.

The temporary matrix will be taken from visual.py
"""
import numpy as np

# Relation of original corner form to the corners final form
corner_number_dict = {
    (0, 10, 40): (9, 13, 41),
    (0, 30, 40): (3, 31, 43),
    (10, 20, 50): (17, 29, 51),
    (30, 40, 50): (37, 49, 59),
    (10, 40, 50): (19, 47, 53),
    (0, 10, 20): (7, 11, 23),
    (0, 20, 30): (1, 21, 33),
    (20, 30, 50): (27, 39, 57)
}

# Relation of original edge form to the edges final form
edge_number_dict = {
    (10, 20): (14, 26),
    (0, 40): (6, 42),
    (20, 30): (24, 36),
    (30, 40): (34, 46),
    (0, 20): (4, 22),
    (40, 50): (48, 56),
    (30, 50): (38, 58),
    (20, 50): (28, 54),
    (0, 30): (2, 32),
    (10, 50): (18, 52),
    (10, 40): (16, 44),
    (0, 10): (8, 12)
}

# Coordinates of all the corner faces
corner_faces = (
    ((0, 0, 0), (2, 0, 0), (3, 0, 2)),
    ((0, 0, 2), (3, 0, 0), (4, 0, 2)),
    ((0, 2, 2), (1, 0, 2), (4, 0, 0)),
    ((0, 2, 0), (1, 0, 0), (2, 0, 2)),
    ((5, 0, 0), (1, 2, 0), (2, 2, 2)),
    ((5, 2, 0), (2, 2, 0), (3, 2, 2)),
    ((3, 2, 0), (5, 2, 2), (4, 2, 2)),
    ((1, 2, 2), (4, 2, 0), (5, 0, 2))
)

# Coordinates of all the edge faces
edge_faces = (
    ((0, 0, 1), (3, 0, 1)),
    ((0, 1, 2), (4, 0, 1)),
    ((0, 2, 1), (1, 0, 1)),
    ((0, 1, 0), (2, 0, 1)),
    ((1, 1, 0), (2, 1, 2)),
    ((2, 1, 0), (3, 1, 2)),
    ((3, 1, 0), (4, 1, 2)),
    ((1, 1, 2), (4, 1, 0)),
    ((1, 2, 1), (5, 0, 1)),
    ((2, 2, 1), (5, 1, 0)),
    ((3, 2, 1), (5, 2, 1)),
    ((4, 2, 1), (5, 1, 2)),
)
# Temporary matrix for testing purposes
temp_matrix = np.array([
    [[40, 20, 0],
     [40, 0, 0],
     [50, 30, 50]],

    [[20, 20, 30],
     [50, 10, 50],
     [50, 0, 10]],

    [[10, 30, 10],
     [0, 20, 20],
     [20, 0, 40]],

    [[30, 10, 0],
     [50, 30, 20],
     [30, 10, 0]],

    [[40, 40, 40],
     [30, 40, 40],
     [20, 10, 50]],

    [[10, 30, 0],
     [10, 50, 50],
     [30, 40, 20]]
])

'''
[[[41 26  3]
  [46  5  6]
  [51 36 59]]

 [[29 24 37]
  [54 15 58]
  [53  2 11]]

 [[13 34 17]
  [ 4 25 28]
  [21  8 47]]

 [[31 14  9]
  [56 35 22]
  [39 16  1]]

 [[49 42 43]
  [38 45 48]
  [23 18 57]]

 [[19 32  7]
  [12 55 52]
  [33 44 27]]]
'''


def numbering(matrix):
    """Convert original matrix to a solvable one."""
    # These access the data structures above for using the relations
    corner = ((0, 1, 2), corner_faces, corner_number_dict)
    edge = ((0, 1), edge_faces, edge_number_dict)

    # Corners then edges
    for settings in (corner, edge):
        # Loop through the pieces in the coordinate data structure
        for piece in settings[1]:
            # Create an empty list for storing the values found
            c = []
            # Loop through the faces per piece
            for face in piece:
                # Append the value for each face of the piece to the list
                c.append(matrix[face[0]][face[1], face[2]])
            # Sort the list lowest to highest
            c.sort()
            # Retrieve final forms for each face
            new_nums = settings[2].get(tuple(c))
            # Loop through faces again
            for face in piece:
                # Retrieve current face value
                facelet = matrix[face[0]][face[1], face[2]]
                # Loop through 0 1 2
                for num in settings[0]:
                    # If the current value of the list is the same
                    # as the current face
                    if c[num] == facelet:
                        # Set value of current face to matching value of c list
                        matrix[face[0]][face[1], face[2]] = new_nums[num]
    # Loop through 0 1 2 3 4 5
    for side in range(6):
        # Add 5 to each middle piece
        matrix[side][1, 1] += 5

    return matrix
