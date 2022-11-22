#!/usr/bin/python3

import time
import os

life = 3
x = 0
y = 0

def print_gameboard(x, y):
    os.system('cls' if os.name == 'nt' else 'clear')

    board = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

    board_width = len(board[0])
    board_height = len(board)

    if x < board_width and y < board_height:
        board[y][x] = "="
    else:
        x = 0
        y = 0

    sg_row = ""
    sg_list = []

    print("+----------+")

    for row in board:
        for column in row:
            sg_row += column
        sg_list.append(sg_row)
        sg_row = ""

    for row in sg_list:
        print(f"|{row}|") # => print("|{}|".format(row))

    print("+----------+")



while life > 0:
    print_gameboard(x, y)

    user_key = input()

    if user_key == 'l':
        if x < 9:
            x = x + 1
        else:
            x = 0

    if user_key == 'k':
        if y < 4:
            y = y + 1
        else:
            y = 0

    time.sleep(0.1)
    
