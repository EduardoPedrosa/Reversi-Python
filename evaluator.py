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
        if(level == 3):
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
                    [-8,-8,-2,-2,-2,-2,-8,-8],
                    [ 8,-2, 1, 1, 1, 1,-2, 8],
                    [ 8,-2, 1, 1, 1, 1,-2, 8],
                    [ 8,-2, 1, 1, 1, 1,-2, 8],
                    [ 8,-2, 1, 1, 1, 1,-2, 8],
                    [-8,-8,-2,-2,-2,-2,-8,-8],
                    [64,-8, 8, 8, 8, 8,-8,64],
                    ]


    def score(self, board, currentDepth, player, opponent):
        whites, blacks, empty = board.count_stones()

        # check wipe out
        if (player == WHITE and whites == 0) or (player == BLACK and blacks == 0):
            return -1000
        if (opponent == WHITE and whites == 0) or (opponent == BLACK and blacks == 0):
            return 1000
            
        score = 0
        # determine weigths according to the number of pieces
        for i in range (0,8):
            for j in range (0,8):
                if(board.board[i][j] == player):
                    score += (self.WEIGHT_MATRIX[i][j])
                if(board.board[i][j] == opponent):
                    score -= (self.WEIGHT_MATRIX[i][j])
        return score
