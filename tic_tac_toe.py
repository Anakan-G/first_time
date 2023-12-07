import os
os.system("cls")

squ = [0,1,2,3,4,5,6,7,8,9]

def draw_board():
    os.system("cls")
    print("Tic-Tac-Toe")
    board = (
        "\n"
        + f"| {squ[1]} | {squ[2]} | {squ[3]} |\n"
        + f"| {squ[4]} | {squ[5]} | {squ[6]} |\n"
        + f"| {squ[7]} | {squ[8]} | {squ[9]} |\n"
    )
    print(board)

    if is_winner()[0]:
        return is_winner()[1]
    
    return None


def is_winner():
    if squ[1] == squ[2] == squ[3]: return (True, squ[1])
    if squ[4] == squ[5] == squ[6]: return (True, squ[4])
    if squ[7] == squ[8] == squ[9]: return (True, squ[7])
    if squ[1] == squ[4] == squ[7]: return (True, squ[1])
    if squ[2] == squ[5] == squ[8]: return (True, squ[2])
    if squ[3] == squ[6] == squ[9]: return (True, squ[3])
    if squ[1] == squ[5] == squ[9]: return (True, squ[1])
    if squ[3] == squ[5] == squ[7]: return (True, squ[3])
    return (False, None)



draw_board()

for turn_num in range(0,9):
    if turn_num in [0,2,4,6,8]:
        player = "X"
    else:
        player = "O"


    x_o = int(input(f"What position for the next '{player}'? "))


    squ[x_o] = player
    winner = draw_board()
    if winner:
        print("The winner is '" + winner + "'")
        break

