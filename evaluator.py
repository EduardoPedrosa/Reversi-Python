from config import BLACK, WHITE, EMPTY
from random import randint

class Evaluator(object):

    def __init__(self, level):
        super().__init__()
        self.level = level
        if(level == 1):
            self.WEIGHT_MATRIX = self.WORST_WEIGHT_MATRIX
        if(level == 2):
            self.WEIGHT_MATRIX = self.MEDIUM_WEIGHT_MATRIX
        if(level == 4):
            self.WEIGHT_MATRIX = self.BEST_WEIGHT_MATRIX

    WORST_WEIGHT_MATRIX = [
                    [ 1, 1, 1, 1, 1, 1, 1, 1],
                    [ 1, 1, 1, 1, 1, 1, 1, 1],
                    [ 1, 1, 1, 1, 1, 1, 1, 1],
                    [ 1, 1, 1, 1, 1, 1, 1, 1],
                    [ 1, 1, 1, 1, 1, 1, 1, 1],
                    [ 1, 1, 1, 1, 1, 1, 1, 1],
                    [ 1, 1, 1, 1, 1, 1, 1, 1],
                    [ 1, 1, 1, 1, 1, 1, 1, 1],
                    ]

    MEDIUM_WEIGHT_MATRIX = [
                    [ 4,-3, 2, 2, 2, 2,-3, 4],
                    [-3,-4,-1,-1,-1,-1,-4,-3],
                    [ 2,-1, 1, 0, 0, 1,-1, 2],
                    [ 2,-1, 0, 1, 1, 0,-1, 2],
                    [ 2,-1, 0, 1, 1, 0,-1, 2],
                    [ 2,-1, 1, 0, 0, 1,-1, 2],
                    [-3,-4,-1,-1,-1,-1,-4,-3],
                    [ 4,-3, 2, 2, 2, 2,-3, 4],
                    ]

    BEST_WEIGHT_MATRIX = [
                    [64,-8, 8, 8, 8, 8,-8,64],
                    [-8,-8, 1, 1, 1, 1,-8,-8],
                    [ 8, 1, 1, 1, 1, 1, 1, 8],
                    [ 8, 1, 1, 1, 1, 1, 1, 8],
                    [ 8, 1, 1, 1, 1, 1, 1, 8],
                    [ 8, 1, 1, 1, 1, 1, 1, 8],
                    [-8,-8, 1, 1, 1, 1,-8,-8],
                    [64,-8, 8, 8, 8, 8,-8,64],
                    ]


    def score(self, startBoard, board, currentDepth, player, opponent):
        """ Determine the score of the given board for the specified player.
        - startBoard the board before any move is made
        - board the board to score
        - currentDepth depth of this leaf in the game tree
        - searchDepth depth used for searches.
        - player current player's color
        - opponent opponent's color
        """

        self.player = player
        self.enemy = opponent
        whites, blacks, empty = board.count_stones()
        deltaBoard = board.compare(startBoard)
        deltaCount = sum(deltaBoard.count_stones())

        # check wipe out
        if (self.player == WHITE and whites == 0) or (self.player == BLACK and blacks == 0):
            return -300
        if (self.enemy == WHITE and whites == 0) or (self.enemy == BLACK and blacks == 0):
            return 300

        score = 0

        # determine weigths according to the number of pieces
        for i in range (0,8):
            for j in range (0,8):
                if(deltaBoard.board[i][j] == self.player):
                    score += self.WEIGHT_MATRIX[i][j]
                if(deltaBoard.board[i][j] == self.enemy):
                    score -= self.WEIGHT_MATRIX[i][j]
        return score
