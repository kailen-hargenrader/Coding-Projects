"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X" or board[i][j] == "O":
                count +=1
    if(terminal(board)):
        return "done"

    elif count % 2 == 0:
        return "X"
    else:
        return "O"
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    temp = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                temp.add((i, j))
    if terminal(board):
        return "done"
    else:
        return temp
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = [board[0].copy(), board[1].copy(), board[2].copy()]
    if newboard[action[0]][action[1]] != None:
        raise NameError("That action is not valid")
    if player(board) == "X":
        newboard[action[0]][action[1]] = "X"
        return newboard
    elif player(board) == "O":
        newboard[action[0]][action[1]] = "O"
        return newboard
    else:
        raise NameError("Game should be finished")
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(len(board)):
        down = 0
        across = 0
        for j in range(len(board[i])):
            if board[i][j] == "X":
                across += 1
            elif board[i][j] == "O":
                across -= 1
            if board[j][i] == "X":
                down += 1
            if board [j][i] == "O":
                down -= 1
            if across == 3 or down == 3:
                return "X"
            elif across == -3 or down == -3:
                return "O"
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "X"
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" or board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "O"
    return None
        
            
                
            
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None and (board[0].count(None) != 0 or board[1].count(None) != 0 or board[2].count(None) != 0):
        return False
    else:
        return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        results = {}
        for action in actions(board):
            results[action] = getcount(result(board, action))
        #print(results)
        best = None
        for number in results:
            if best == None:
                best = number
            else:
                if player(board) == "X":
                    if results.get(number) > results.get(best):
                        best = number
                else:
                    if results.get(number) < results.get(best):
                        best = number
        return best
            
        
def getcount(board):
    newboard = board
    if terminal(newboard) == True:
        #print("Here!")
        return utility(board)
    else: 
        count = None
        for action in actions(newboard):
            
            score = getcount(result(newboard, action))
            
            if player(newboard) == "X":
                #print("max")
                if count == None or score > count:
                    count = score
            else:
                #print("min")
                if count == None or score < count:
                    count = score
            #print(newboard)
            #print(action)
            #print(score)
        #print(count)
            #count += getcount(result(newboard, action))/len(actions(newboard))
        return count
    

    
    raise NotImplementedError
