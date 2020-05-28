from board import Board
from os import system

if __name__ == "__main__":
    system('clear')
    b = Board()
    print("TicTacToe!")
    print(b.get_board())
    print("Options: 1-9, x (to exit)")
    option = ""
    while option.lower() != "x":
        option = input("You: ")
        b.set_value_by_index("x", option)
        system('clear')
        print(b.get_board())
