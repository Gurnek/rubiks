'''
this will be for controlling the cameras and analyzing the pictures, then
creating a ndarray from the data collected.
'''
import numpy as np

#relation of original corner form to the corners final form
corner_number_dict = {
    (0, 10, 40) : (9, 13, 41),
    (0, 30, 40) : (3, 31, 43),
    (10, 20, 50) : (17, 29, 51),
    (30, 40, 50) : (37, 49, 59),
    (10, 40, 50) : (19, 47, 53),
    (0, 10, 20) : (7, 11, 23),
    (0, 20, 30) : (1, 21,33),
    (20, 30, 50) : (27, 39, 57)
}

#relation of original edge form to the edges final form
edge_number_dict = {
    (10, 20) : (14, 26),
    (0, 40) : (6, 42),
    (20, 30) : (24, 36),
    (30, 40) : (34, 46),
    (0, 20) : (4, 22),
    (40, 50) : (48, 56),
    (30, 50) : (38, 58),
    (20, 50) : (28, 54),
    (0, 30) : (2, 32),
    (10, 50) : (18, 52),
    (10, 40) : (16, 44),
    (0, 10) : (8, 12)
}

#coordinates of all the corner faces
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

#coordinates of all the edge faces
edge_faces = (
    ((0, 0, 1), (3, 0, 1)),
    ((0, 1, 2), (4, 0, 1)),
    ((0, 2, 1), (1, 0, 1)),
    ((0, 1, 0), (2, 0, 1)),
    ((1, 1, 0), (2, 1, 2)),
    ((2, 1, 0), (3, 1, 2)),
    ((3, 1, 0), (4, 1, 2)),
    ((1, 1, 2), (4, 1, 0)),
    ((1, 2 ,1), (5, 0, 1)),
    ((2, 2, 1), (5, 1, 0)),
    ((3, 2, 1), (5, 2, 1)),
    ((4, 2, 1), (5, 1, 2)),
)
#temporary matrix for testing purposes
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

#function used to convert original matrix to a solvable matrix
def numbering(matrix):
    #these access the data structures above for using the relations
    corner = ((0, 1, 2), corner_faces, corner_number_dict)
    edge = ((0, 1), edge_faces, edge_number_dict)

    #corners then edges
    for settings in (corner, edge):
        #loop through the pieces in the coordinate data structure
        for piece in settings[1]:
            #create an empty list for storing the values found
            c = []
            #loop through the faces per piece
            for face in piece:
                #append the value for each face of the piece to the list
                c.append(matrix[face[0]][face[1], face[2]])
            #sort the list lowest to highest
            c.sort()
            #retrieve final forms for each face
            new_nums = settings[2].get(tuple(c))

            #loop through faces again
            for face in piece:
                #retrieve current face value
                facelet = matrix[face[0]][face[1], face[2]]
                #loop through 0 1 2
                for num in settings[0]:
                    #if the current value of the list is the same as the current face
                    if c[num] == facelet:
                        #set value of current face to matching value of c list
                        matrix[face[0]][face[1], face[2]] = new_nums[num]
    #loop through 0 1 2 3 4 5
    for side in range(6):
        #add 5 to each middle piece
        matrix[side][1, 1] += 5
    
    return matrix