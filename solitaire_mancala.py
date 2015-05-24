"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

# URL = #user40_t2XbRk5szUCPTV7.py

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._configuration = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._configuration = []
        for house in range(0, len(configuration)):
            self._configuration.append(configuration[house])
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        right = len(self._configuration) - 1
        board_str = "["
        while right > 0:
            board_str += str(self._configuration[right])
            board_str += ", "
            right -= 1
        board_str += str(self._configuration[right])
        board_str += "]"
        return board_str
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._configuration[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for house in range(1, len(self._configuration)):
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
            self._configuration[house_num] = 0
            seeds = house_num
            while seeds > 0:
                self._configuration[seeds - 1] += 1    
                seeds -= 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house in range(1, len(self._configuration)):
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
        test_conf = self._configuration
        move_set = []
        def test_get_num_seeds(house_num):
            """
            Same like in the other
            """
            return test_conf[house_num]    
        def test_is_legal_move(house_num):
            """
            Same like in the other
            """
            if house_num == 0:
                return False
            elif test_get_num_seeds(house_num) == house_num:
                return True
            else:
                return False
        def test_choose_move():
            """
            Same like in the other
            """
            for house in range(1, len(test_conf)):
                if test_is_legal_move(house):
                    return house
            return 0
        def test_is_game_won():
            """
            Same like in the other
            """
            for house in range(1, len(test_conf)):
                if test_get_num_seeds(house) != 0:
                    return False
            return True
        def test_apply_move(house_num):
            """
            Same like in the other
            """
            if test_is_legal_move(house_num):
                test_conf[house_num] = 0
                seeds = house_num
                while seeds > 0:
                   test_conf[seeds - 1] += 1    
                   seeds -= 1
    
        while test_is_game_won() == False:
            if test_choose_move() == 0:
                return move_set
            else:
                house = test_choose_move();
                test_apply_move(house)
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
