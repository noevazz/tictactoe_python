from board import Board
from random import choice


class TicTacToe(Board):
    def __init__(self):
        self.__moves = 0
        super().__init__()
    
    def set_game_mode(self, game_mode):
        if game_mode in ["1", "2"]:
            self.game_mode = game_mode
            return True
        else:
            return False
    
    def play(self):
        print(self.get_quadrants())
        if self.game_mode == "1":
            self.__play_1vs1()
        elif self.game_mode == "2":
            self.__play_pcvsyou()
    
    def __play_pcvsyou(self):
        print(super().get_board())
        while True:
            self.__move_player("Player 1", "x")
            if self.__check_winner() != None:
                print("the winner is", "PC" if self.__check_winner()=="o" else "Player 1")
                break

            if self.__moves == 9:
                print("WOW!, IT'S A MATCH!!")
                self.__reset()
                break

            self.__move_player("PC", "o", auto=True)
            print(super().get_board())
            if self.__check_winner() != None:
                print("the winner is", "PC" if self.__check_winner()=="o" else "Player 1")
                break
    
    
    def __play_1vs1(self):
        print(super().get_board())
        while True:
            self.__move_player("Player 1", "x")
            if self.__check_winner() != None:
                print("the winner is", self.__check_winner())
                break

            if self.__moves == 9:
                print("WOW!, IT'S A MATCH!!")
                self.__reset()
                break
            print(super().get_board())
            self.__move_player("Player 2", "o")
            if self.__check_winner() != None:
                print("the winner is", self.__check_winner())
                break
            print(super().get_board())
    
    def __move_player(self, player_name, symbol, auto=False):
        option = None
        if auto:
            option = choice( ( [key for key, val_dict in self.get_quadrants().items() if val_dict["value"] not in ["x", "o"]] ) )
            #print( [key for key, val_dict in self.get_quadrants().items() if val_dict["value"] in ["x", "o"]] )
        else:
            option = input(f"{player_name} [{symbol}]: ")
        super().set_quadrant(option, symbol)
        self.__moves += 1
    
    def __check_if_available(self, quadrant):
        return self.get_quadrants()[quadrant]["index"] in ["x", "o"]

    def __reset(self):
        self.__moves = 0
    
    def __check_winner(self):
        """
        Returns None if there is no winner
        Returns "x" or "o" depends of the winner
        """
        winner_options = [[1,2,3], # Horizontal line #1
                          [4,5,6], # Horizontal line #2
                          [7,8,9], # Horizontal line #3
                          [1,4,7], # Vertical line #1
                          [2,5,8], # Vertical line #2
                          [3,6,9], # Vertical line #3
                          [1,5,9], # Backslash
                          [7,5,3]] # Forward slash
        for option in winner_options:
            if super().get_quadrants()[ str(option[0]) ]["value"] == super().get_quadrants()[ str(option[1]) ]["value"] and \
                super().get_quadrants()[ str(option[0]) ]["value"] == super().get_quadrants()[ str(option[2]) ]["value"]:
               return super().get_quadrants()[ str(option[0]) ]["value"]
        return None

if __name__ == "__main__":
    gm = None
    game = TicTacToe()
    while game.set_game_mode(gm) == False:
        gm = input("Game mode [1=1vs1, 2=PCvsYou]: ")
    game.play()