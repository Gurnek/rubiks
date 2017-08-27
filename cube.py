'''
this file houses the functions for turning the cube and the login for reading and
executing the solve string. It also has a virtual cube used for testing the move functions
'''

import numpy as np
from solver import *
from visual import numbering, temp_matrix
import time
'''
0 = top = white
1 = front = red
2 = left = green
3 = back = orange
4 = right = blue
5 = bottom = yellow
'''

#creating the cube matrix
cube = np.array([
    [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]],

    [[20, 21, 22],
     [23, 24, 25],
     [26, 27, 28]],

    [[30, 31, 32],
     [33, 34, 35],
     [36, 37, 38]],

    [[40, 41, 42],
     [43, 44, 45],
     [46, 47, 48]],

    [[50, 51, 52],
     [53, 54, 55],
     [56, 57, 58]],

    [[60, 61, 62],
     [63, 64, 65],
     [66, 67, 68]]
])
#Whether the program should move the motors or not
machine = False

#General function for turning the face in the parameter
def turnFace(face, direction):
    #If the motors need to be turned
    if machine == True:
        pass
    else:
        #these next 4 lines select 4 rows of facelets that will be turned in the face
        top = tuple(cube[face][0, :])
        right = tuple(cube[face][:, 2])
        down = tuple(cube[face][2, :])
        left = tuple(cube[face][:, 0])

        #if clockwise
        if direction == True:
            cube[face][0, :] = np.flipud(left)
            cube[face][:, 2] = top
            cube[face][2, :] = np.flipud(right)
            cube[face][:, 0] = down

        #if counterclockwise
        else:
            cube[face][0, :] = right
            cube[face][:, 2] = np.flipud(down)
            cube[face][2, :] = left
            cube[face][:, 0] = np.flipud(top)

#function for the up movement
def up(direction):
    #Turn the motor
    if machine == True:
        pass
    #move the matrix
    else:
        #defining rows of the cube
        front_top = tuple(cube[1][0, :])
        left_top = tuple(cube[2][0, :])
        back_top = tuple(cube[3][0, :])
        right_top = tuple(cube[4][0, :])

        #if clockwise
        if direction == True:
            #Select sides that need to be changed in reference to their new side
            sides = {0 : right_top, 1 : front_top, 2 : left_top, 3 : back_top}

            #turn the face clockwise
            turnFace(0, True)
        #counterclockwise
        else:
            #Select sides that need to be changed in reference to their new side
            sides = {0 : left_top, 1 : back_top, 2 : right_top, 3 : front_top}

            #turn the face counterclockwise
            turnFace(0, False)

            #move the matrix
            for side in range(4):
                #Changing the rows
                cube[side + 1][0, :] = sides[side]
#if direction is true, clockwise, if direction is false, counterclockwise
def down(direction):
    if machine == True:
        pass
    else:
        front_bot = tuple(cube[1][2, :])
        left_bot = tuple(cube[2][2, :])
        back_bot = tuple(cube[3][2, :])
        right_bot = tuple(cube[4][2, :])

        if direction == True:
            sides = {0 : left_bot, 1 : back_bot, 2 : right_bot, 3 : front_bot}

            turnFace(5, True)

        else:
            sides = {0 : right_bot, 1 : front_bot, 2 : left_bot, 3 : back_bot}

            turnFace(5, False)

            for side in range(4):
                cube[side + 1][2, :] = sides[side]

def front(direction):
    if machine == True:
        pass
    else:
        up_bot = tuple(cube[0][2, :])
        left_right = tuple(cube[2][:, 2])
        down_top = tuple(cube[5][0, :])
        right_left = tuple(cube[4][:, 0])

        if direction == True:
            cube[0][2, :] = np.flipud(left_right)
            cube[2][:, 2] = down_top
            cube[4][:, 0] = up_bot
            cube[5][0, :] = np.flipud(right_left)

            turnFace(1, True)

        else:
            cube[0][2, :] = right_left
            cube[2][:, 2] = np.flipud(up_bot)
            cube[4][:, 0] = np.flipud(down_top)
            cube[5][0, :] = left_right

            turnFace(1, False)

def left(direction):
    if machine == True:
        pass
    else:
        top_left = tuple(cube[0][:, 0])
        front_left = tuple(cube[1][:, 0])
        down_left = tuple(cube[5][:, 0])
        back_right = tuple(cube[3][:, 2])

        if direction == True:
            cube[0][:, 0] = np.flipud(back_right)
            cube[1][:, 0] = top_left
            cube[5][:, 0] = front_left
            cube[3][:, 2] = np.flipud(down_left)

            turnFace(2, True)

        else:
            cube[0][:, 0] = front_left
            cube[1][:, 0] = down_left
            cube[5][:, 0] = np.flipud(back_right)
            cube[3][:, 2] = np.flipud(top_left)

            turnFace(2, False)

def right(direction):
    if machine == True:
        pass
    else:
        top_right = tuple(cube[0][:, 2])
        front_right = tuple(cube[1][:, 2])
        down_right = tuple(cube[5][:, 2])
        back_left = tuple(cube[3][:, 0])

        if direction == True:
            cube[0][:, 2] = np.flipud(front_right)
            cube[1][:, 2] = down_right
            cube[5][:, 2] = np.flipud(back_left)
            cube[3][:, 0] = np.flipud(top_right)

            turnFace(4, True)
        else:
            cube[0][:, 2] = np.flipud(back_left)
            cube[1][:, 2] = top_right
            cube[5][:, 2] = front_right
            cube[3][:, 0] = np.flipud(down_right)

            turnFace(4, False)

def back(direction):
    if machine == True:
        pass
    else:
        top_top = tuple(cube[0][0, :])
        left_left = tuple(cube[2][:, 0])
        down_down = tuple(cube[5][2, :])
        right_right = tuple(cube[4][:, 2])

        if direction == True:
            cube[0][0, :] = np.flipud(right_right)
            cube[2][:, 0] = top_top
            cube[5][2, :] = np.flipud(left_left)
            cube[4][:, 2] = down_down

            turnFace(3, True)

        else:
            cube[0][0, :] = left_left
            cube[2][:, 0] = np.flipud(down_down)
            cube[5][2, :] = right_right
            cube[4][:, 2] = np.flipud(top_top)

            turnFace(3, False)

def readsol(sol):
    #mapping of string characters to the functions they represent
    moves = {
        'u' : up(True),
        'd' : down(True),
        'f' : front(True),
        'l' : left(True),
        'r' : right(True),
        'b' : back(True),
        'U' : up(False),
        'D' : down(False),
        'F' : front(False),
        'L' : left(False),
        'R' : right(False),
        'B' : back(False),
    }

    #moves through sol string and adds matching function call to exec_str
    for letter in sol:
        moves.get(letter)

    #start to move the motors
    machine == True

#if this is the file called
if __name__ == '__main__':
    print('Enter solve to start the program')
    command = input()
    start = time.time()
    if command = 'solve':
        readsol('uUdDfFlLrRbBuUdDfFlLrRbBuUdDfFlLrRbBuUdDfFlLrRbBuUdDfFlLrRbBuUdDfFlLrRbBuUdDfFlLrRbBuUdDfFlLrRbB')
        print((time.time() - start) * 1000)
