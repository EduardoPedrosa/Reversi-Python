# Minimax module
# Implements a generic minimax with alpha-beta
# prunning algorithm for games like chess or reversi.
# Thu Feb 18 21:54:38 Humberto Pinheiro
from math import inf
from config import BLACK, WHITE

def change_color(color):
    if color == BLACK:
        return WHITE
    else:
        return BLACK

class Minimax(object):

    def __init__(self, heuristic_eval, aiPlayer):
        """ Create a new minimax object
        player - current player's color
        opponent - opponent's color
        """
        self.aiPlayer = aiPlayer #color of the ai in the game
        self.heuristic_eval = heuristic_eval
    
    def minimax(self, board, parentBoard, depth, player):
        #calculating if it's a leaf node:
        childrenQuantity = sum(1 for child in board.next_states(player))
        
        if ((childrenQuantity == 0) or (depth == 0)): ##If it's a leaf node or depth == 0
            return (self.heuristic_eval(parentBoard, board, depth, player, change_color(player)), board)
        
        
        if player == self.aiPlayer:
            
            alfa = -inf
            for child in board.next_states(player):
                bestChild = child
                score, board = self.minimax(child, board, depth-1, change_color(player))
                alfa = max(alfa, score)
                if alfa == score:
                    bestChild = board
            print('Weight: ' + str(alfa))
            return (alfa, bestChild)
        else:

            alfa = inf
            for child in board.next_states(player):
                bestChild = child
                score, board = self.minimax(child, board, depth-1, change_color(player))
                alfa = min(alfa, score)
                if alfa == score: 
                    bestChild = board
            return (alfa, bestChild)    
        
        
    # # error: always return the same board in same cases
    # def minimax(self, board, parentBoard, depth, player, opponent,
    #             alfa=-INFINITY, beta=INFINITY):
    #     bestChild = board
    #     if depth == 0:
    #         return (self.heuristic_eval(parentBoard, board, depth,
    #                                     player, opponent), board)
    #     for child in board.next_states(player):
    #         score, newChild = self.minimax(
    #             child, board, depth - 1, opponent, player, -beta, -alfa)
    #         score = -score
    #         if score > alfa:
    #             alfa = score
    #             bestChild = child
    #         if beta <= alfa:
    #             break
    #     return (self.heuristic_eval(board, board, depth, player,
    #                                 opponent), bestChild)
