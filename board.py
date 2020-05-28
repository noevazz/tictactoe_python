class Board:
    def __init__(self):
        self.__board = "     |     |\n  1  |  2  |  3\n_____|_____|____\n     |     |\n  4  |  5  |  6\n_____|_____|_____\n     |     |\n  7  |  8  |  9\n     |     |    "
        self.__index_cuadrant = {self.__board[index]:index for index in range(len(self.__board)) if self.__board[index].isnumeric() }

    def get_index_cuadrant(self):
        return self.__index_cuadrant

    def set_value_by_index(self, value, index):
        index = str(index)
        self.__board = self.__board[:self.__index_cuadrant[index]] + value + self.__board[self.__index_cuadrant[index]+1:]

    def get_board(self):
      return self.__board

    def set_reset(self):
        self.__board = "     |     |\n  1  |  2  |  3\n_____|_____|____\n     |     |\n  4  |  5  |  6\n_____|_____|_____\n     |     |\n  7  |  8  |  9\n     |     |    "
        self.__index_cuadrant = {self.__board[index]:index for index in range(len(self.__board)) if self.__board[index].isnumeric() }


if __name__ == "__main__":
    b = Board()
    b.set_value_by_index("/", 3)
    b.set_value_by_index("/", 5)
    b.set_value_by_index("/", 7)
    print(b.get_board())
    print("#"*17)
    b.set_reset()
    print(b.get_board())
