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
    
    def minimax(self, board, currentDepth, player):
        
        #calculating if it's a leaf node:
        childrenQuantity = sum(1 for child in board.next_states(player))
        oponent = change_color(player)

        if ((childrenQuantity == 0) or (currentDepth == 0)): ##If it's a leaf node or currentDepth == 0
            print('Nível: ' + str(currentDepth) + ' Score: ' + str(self.heuristic_eval(board, currentDepth, player, oponent)))
            return (self.heuristic_eval(board, currentDepth, player, oponent), board)
        
        bestChild = board
        if player != self.aiPlayer:    #Maximizar
            alfa = -inf
            for child in board.next_states(player):
                score, childBoard = self.minimax(child, currentDepth-1, oponent)
                #score = -score
                if score > alfa:
                    alfa = score
                    bestChild = child
        else:   #Minimizar
            alfa = inf
            for child in board.next_states(player):
                score, childBoard = self.minimax(child, currentDepth-1, oponent)
                #score = -score
                if score < alfa:
                    alfa = score
                    bestChild = child
        print('Nível: ' + str(currentDepth) + ' Score: ' + str(alfa))
        return (alfa, bestChild)