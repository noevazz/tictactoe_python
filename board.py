class Board:
    def __init__(self):
        self.__BOARD ="""\
     |     |
  1  |  2  |  3
_____|_____|____
     |     |
  4  |  5  |  6
_____|_____|_____
     |     |
  7  |  8  |  9
     |     |"""
        self.__QUADRANTS = {self.__BOARD[i]:{"index":i, "value":i} for i in range(len(self.__BOARD)) if self.__BOARD[i].isnumeric() }
        # self.__CUADRANTS = {'1': 15, '2': 21, '3': 27, '4': 61, '5': 67, '6': 73, '7': 108, '8': 114, '9': 120}
        # The key represents the cuadrant
        # The value represents its index in the string
        print(self.__QUADRANTS)
        self.__board = self.__BOARD
        self.__quadrants = self.__QUADRANTS

    def get_quadrants(self):
        return self.__quadrants

    def set_quadrant(self, quadrant, value):
        quadrant = str(quadrant)
        self.__board = self.__board[:self.__quadrants[quadrant]["index"]] +\
             value + self.__board[self.__quadrants[quadrant]["index"]+1:]
        self.__quadrants[quadrant]["value"] = value

    def get_board(self):
      return self.__board

    def reset_board(self):
        self.__board = self.__BOARD
        self.__quadrants = self.__QUADRANTS


if __name__ == "__main__":
    # Examples
    b = Board()
    b.set_quadrant(3, "/")
    b.set_quadrant(5, "/")
    b.set_quadrant(7, "/")
    print(b.get_board())

    print("#"*17)

    b.reset_board()
    print(b.get_board())
