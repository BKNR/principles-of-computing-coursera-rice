"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

# URL = #user40_w4MeizzGOm7VLtX.py

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = []
        for house in range(0, len(configuration)):
            self._board.append(configuration[house])
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        right = len(self._board) - 1
        board_str = "["
        while right > 0:
            board_str += str(self._board[right])
            board_str += ", "
            right -= 1
        board_str += str(self._board[right])
        board_str += "]"
        return board_str
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for house in range(1, len(self._board)):
            if self.get_num_seeds(house) != 0:
                return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num == 0:
            return False
        elif self.get_num_seeds(house_num) == house_num:
            return True
        else:
            return False
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            self._board[house_num] = 0
            seeds = house_num
            while seeds > 0:
                self._board[seeds - 1] += 1    
                seeds -= 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house in range(1, len(self._board)):
            if self.is_legal_move(house):
                return house
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        temp_game = SolitaireMancala()
        temp_game.set_board(self._board)
        move_set = []
        while temp_game.is_game_won() == False:
            if temp_game.choose_move() == 0:
                return move_set
            else:
                house = temp_game.choose_move();
                temp_game.apply_move(house)
                move_set.append(house)
        return move_set
 

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    # add more tests here
    
#test_mancala()


# Import GUI code once you feel your code is correct
# import poc_mancala_gui 
# poc_mancala_gui.run_gui(SolitaireMancala())
