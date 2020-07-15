from board import Board

class Game(Board):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    b = Game()
    print(b.get_board())
    option = ""
    while True:
        option = input("You: ")
        if option.lower() == "x":
            break
        b.set_quadrant(option, "x")
        print(b.get_board())
