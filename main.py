from board import Board

class Game(Board):
    def __init__(self):
        super().__init__()
        self.board_status = {str(k):k for k in range(1,10)}
        print(self.board_status["2"])

if __name__ == "__main__":
    b = Game()
    print(b.get_board())
    option = ""
    while True:
        option = input("You: ")
        if option.lower() == "x":
            break
        b.set_value_by_quadrant("x", option)
        print(b.get_board())
