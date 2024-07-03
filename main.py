import random
import numpy as np

LINES = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8],
                  [0, 3, 6],
                  [1, 4, 7],
                  [2, 5, 8],
                  [0, 4, 8],
                  [2, 4, 6]]).astype(int)


def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")


def tic(board, index):
    if board[index] == " ":
        board[index] = "X"
    else:
        print("Field already ocupied. Please, choose another.")


def tac(board, index):
    if board[index] == " ":
        board[index] = "O"
    else:
        print("Field already ocupied. Please, choose another.")


def is_draw(board):
    return np.all(board != " ")


def tic_wins(board):
    for line in LINES:
        if np.all(board[line] == "X"):
            return True
    return False


def tac_wins(board):
    for line in LINES:
        if np.all(board[line] == "O"):
            return True
    return False


def place_shot(board):
    available_shots = np.argwhere(board == " ")
    if len(available_shots) > 0:
        if board[4] == " ":
            print("The computer shoots in the middle!")
            board[4] = "O"
        empty_lines = np.empty((0, 3), int)
        prospective_lines = np.empty((0, 3), int)
        for line in LINES:
            if np.sum(board[line] == "O") == 2 and np.all(board[line] != "X"):
                shot = line[np.argwhere(board[line] == " ")]
                print(f"The computer shoots the finishing line {shot + 1}")
                board[shot] = "O"
                return
            if np.sum(board[line] == "X") == 2 and np.all(board[line] != "O"):
                shot = line[np.argwhere(board[line] == " ")]
                print(f"The computer shoots the dangerous line {shot + 1}")
                board[shot] = "O"
                return
            if np.all(board[line] == " "):
                empty_lines = np.append(empty_lines, [line], axis=0)
            if np.all(board[line] != "X") and np.any(board[line] == "O"):
                prospective_lines = np.append(prospective_lines, [line], axis=0)
        if len(prospective_lines) == 0:
            shot = random.choice(np.intersect1d(available_shots, np.array([0, 2, 6, 8])))
            print(f"The computer shoots any free corner {shot + 1}")
            board[shot] = "O"
            return
        for i in available_shots:
            lines_with_i = [i in line for line in prospective_lines]
            if np.sum(lines_with_i) > 1:
                shot = i
                print(f"The computer shoots for the win {shot + 1}")
            else:
                shot = random.choice(np.intersect1d(prospective_lines, available_shots))
                print(f"The computer shoots for the win {shot + 1}")
            board[shot] = "O"
            return






board = np.full(9, " ")
game_on = True

print("Welcome to the Tic Tac Toe game!")

is_starting = random.randint(0, 1)
if is_starting == 0:
    print("The computer starts!")
    tac(board, 4)
    print_board(board)
else:
    print("The player starts!")

while game_on:
    coord = int(input("Place your shot (1 to 9): ")) - 1
    tic(board, coord)
    print_board(board)

    if tic_wins(board):
        game_on = False
        print("You win!")
    if tac_wins(board):
        game_on = False
        print("You lose!")
    if is_draw(board):
        game_on = False
        print("It is a draw")

    place_shot(board)
    print_board(board)

    if tic_wins(board):
        game_on = False
        print("You win!")
    if tac_wins(board):
        game_on = False
        print("You lose!")
    if is_draw(board):
        game_on = False
        print("It is a draw")
