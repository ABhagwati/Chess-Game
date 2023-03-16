from ChessBoardGUI import ChessBoard
from ChessPieces import Piece
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from Pawn import Pawn
from King import King
from Rook import Rook
import time
import copy
    

def setupGame(colorList, board): #NOTE DEFINE pieceDicts AND CONSIDER DICTIONARY VS ARRAY
    """Instantiates all the pieces within a list of dictionaries, one for each color."""

##    place pieces on board GUI()
##    instantiate all pieces()
    pieceDicts = [{}, {}]
    for i in range(0,2):        # sets the prefix for each image based on its color
        if i == 0:
            imageColor = "chessW"
        else:
            imageColor = "chessB"
            
        backrow = 1+i*7 # defines back row for each color
        pawnrow = 2+i*5 # defines pawn row for each color
        pieceDicts[i]["K" ] = King((5,backrow),colorList[i], "king", imageColor+"K.png")
        board.drawPiece((5,backrow), pieceDicts[i]["K" ].getImageName())
        
        pieceDicts[i]["Q" ] = Queen((4,backrow),colorList[i], "queen", imageColor+"Q.png")
        board.drawPiece((4,backrow), pieceDicts[i]["Q" ].getImageName())
        
        pieceDicts[i]["Ra"] = Rook((1,backrow),colorList[i], "rook", imageColor+"R.png")
        board.drawPiece((1,backrow), pieceDicts[i]["Ra"].getImageName())
        
        pieceDicts[i]["Rh"] = Rook((8,backrow),colorList[i], "rook", imageColor+"R.png")
        board.drawPiece((8,backrow), pieceDicts[i]["Rh"].getImageName())
        
        pieceDicts[i]["Bc"] = Bishop((3,backrow),colorList[i], "bishop", imageColor+"B.png")
        board.drawPiece((3,backrow), pieceDicts[i]["Bc"].getImageName())
        
        pieceDicts[i]["Bf"] = Bishop((6,backrow),colorList[i], "bishop", imageColor+"B.png")
        board.drawPiece((6,backrow), pieceDicts[i]["Bf"].getImageName())
        
        pieceDicts[i]["Nb"] = Knight((2,backrow),colorList[i], "knight", imageColor+"N.png")
        board.drawPiece((2,backrow), pieceDicts[i]["Nb"].getImageName())
        
        pieceDicts[i]["Ng"] = Knight((7,backrow),colorList[i], "knight", imageColor+"N.png")
        board.drawPiece((7,backrow), pieceDicts[i]["Ng"].getImageName())
        
        for j in range(1, 9):   # defines all pawns
            pieceDicts[i]["P"+str(j)] = Pawn((j,pawnrow),colorList[i], "pawn", imageColor+"P.png")
            board.drawPiece((j,pawnrow), pieceDicts[i]["P"+str(j)].getImageName())

    return pieceDicts

def move(board, currentColor, pieceDicts, previousMessage, colorList):
    """Completes whole sequence of printing to the board, waiting for user to click,
       validating the user's click on a piece based on whether it has possible moves
       and checking for check,
       highlighting those possible moves, validating the user's second click based on
       if it's in the pool of valid moves, and executing the second move with undrawing
       and drawing, including promotion."""
    #Determines whether there is a check against friendly before the move.
    if previousMessage != "": # handles condition that this is the first move in the game.
        if isChecked(currentColor, pieceDicts): #if it is checked, print different msg
            if outOfCheckMoves(currentColor, pieceDicts):
                previousMessage = previousMessage + " (Check)"
            else:
                previousMessage = previousMessage + " -- Checkmate!"
                board.printMsg(previousMessage)
                return 1, ""

        previousMessage = previousMessage + " -- it is now "+ colorList[currentColor] +"'s move."
        board.printMsg(previousMessage) 

    # What happens after piece is clicked:
    legalClick, legalMove = False, False # when these are true, continue but until they are true, don't continue
    while not (legalMove and legalClick):

        legalClick, legalMove = False, False
        
        p = board.getWin().getMouse() # gets first mouse click 
        while not (board.isClickOn8x8(p) or board.quitButtonClicked(p)): # if wrong click location, get click again
            p = board.getWin().getMouse()

        if board.getQuitStatus(): # checks for quit clicks
            return -1, ""
        
        clickedSq = board.getClickedSquare(p) # get the square thats been clicked
        clickedPiece = ""
        for name, piece in pieceDicts[currentColor].items(): # associate this square and the piece
            if piece.getPos() == clickedSq:
                clickedPiece = piece
                clickedPieceName = name
                break
        if clickedPiece == "": # if it's empty then prompt to click again
            board.printMsg("Please click on a "+colorList[currentColor]+" piece!")
            continue
        else:
            startingValidMoves = clickedPiece.getValidMoves(currentColor, pieceDicts, False, False)
            validMoves = copy.deepcopy(startingValidMoves)  # deepcopy is important here - if tempDicts changes,
            if validMoves != []:                            # really don't want pieceDicts to change at all
                for move in startingValidMoves:             # since this is all hypothetical
                    captureName = ""
                    tempDicts = copy.deepcopy(pieceDicts)
                    thePiece = tempDicts[currentColor][clickedPieceName]
                    thePiece.makeMove(move)                 # makes move on imaginary board
                    if thePiece.getPromoteStatus():         # PROMOTION
                        queenName = "Q"+clickedPieceName[1]
                        if currentColor == 0:
                            imageColor = "chessW"
                        else:
                            imageColor = "chessB"           # based on pawn's info, create Q piece in dictionary
                        tempDicts[currentColor][queenName] = Queen(thePiece.getPos(),colorList[currentColor], "queen", imageColor+"Q.png")
                        del tempDicts[currentColor][clickedPieceName]

                    for name, piece in tempDicts[1-currentColor].items():
                        if piece.getPos() == move:          # capture
                            captureName = name

                    if captureName != "":
                        del tempDicts[1-currentColor][captureName]                            
                    if not isChecked(currentColor, tempDicts):
                        legalClick = True                   # prevent user from checking self
                    else:
                        validMoves.remove(move)
          
        if not legalClick:
            board.printMsg("That piece does not have any legal moves -- please pick another piece")
            continue

        for sq in validMoves:
            board.highlight(convertToString(sq))            # highlight valid moves          
        board.printMsg("Please select a move from the indicated options.")

        p = board.getWin().getMouse()                       # wait for 2nd click
        while not (board.isClickOn8x8(p) or board.quitButtonClicked(p)):
            p = board.getWin().getMouse()

        if board.getQuitStatus():                           # check for quit button click
            return -1, ""
        destSq = board.getClickedSquare(p)        
        captured = ""        
        for dest in validMoves:                             # iterates through all valid moves
            if destSq == dest:
                legalMove = True
                board.undrawPiece(convertToString(clickedSq))

                thePiece = pieceDicts[currentColor][clickedPieceName]
                thePiece.makeMove(dest)                     # moves clicked piece
                if thePiece.getPromoteStatus():             # handles promotion - turns into queen
                    queenName = "Q"+clickedPieceName[1]
                    if currentColor == 0:
                        imageColor = "chessW"
                    else:
                        imageColor = "chessB"               # undraws pawn, redraws queen
                    pieceDicts[currentColor][queenName] = Queen(thePiece.getPos(),colorList[currentColor], "queen", imageColor+"Q.png")
                    clickedPiece = pieceDicts[currentColor][queenName]
                    del pieceDicts[currentColor][clickedPieceName]
        
                for name, piece in pieceDicts[1-currentColor].items():
                    if piece.getPos() == dest:              # undraws piece, redraws at destination
                        del pieceDicts[1-currentColor][name]
                        board.undrawPiece(convertToString(dest))
                        captured = colorList[currentColor]+"'s "+clickedPiece.getType()+" captured "+ colorList[1-currentColor]+"'s "+piece.getType()+" at "+ convertToString(dest)
                        break

                board.drawPiece(dest,clickedPiece.getImageName())
                
                if captured == "":                          # creates message that prints later
                    currentMessage = colorList[currentColor]+" moved "+clickedPiece.getType()+" to "+convertToString(dest)
                else:
                    currentMessage = captured                
                break

        if not legalMove:                                   # error message if user doesn't click a valid move
            board.printMsg("That is not a valid move. Please try again.")
        for sq in validMoves:
            board.unhighlight(convertToString(sq))          # unhighlights valid moves if it is executed
            
    return 0, currentMessage

def outOfCheckMoves(currentColor, pieceDicts):
    """determines whether or not it is possible for a team to
       make a move that brings it out of being checked"""

    # move king - sees if king can be moved to uncheck
    enemyMoves, checkingPieces = getEnemyMoves(currentColor,pieceDicts,True,True)
    for move in pieceDicts[currentColor]["K"].getValidMoves(currentColor, pieceDicts, False, True):
        if move not in enemyMoves:
            return True
        
    # capture checking piece - sees if a piece can capture the checking peice(s)    
    noKingFriendlyCaptures, noKingCaptPieces = getEnemyMoves(1-currentColor,pieceDicts,False,True)
    for piece in checkingPieces:
        if piece.getPos() in noKingFriendlyCaptures:
            return True
    
    # block checking piece - sees if a piece can block the path of a checking piece
    # if it is a queen, rook, or bishop
    noKingFriendlyMoves, noKingChPieces = getEnemyMoves(1-currentColor,pieceDicts,False,False)
    
    for piece in checkingPieces:            # checks if any possible moves are between
                                            # checking piece and king (straight,
                                            # diagonal)
        if piece.getType() in ["queen", "rook", "bishop"]:
            x0, y0 = piece.getPos()
            x1, y1 = pieceDicts[currentColor]["K"].getPos()

            if (x0 == x1 and abs(x1-x0)):
                for y in range(min(y0,y1) + 1, max(y0,y1)):
                    if (x0,y) in noKingFriendlyMoves:
                       return True

            if (y0 == y1 and abs(y1-y0)):
                for x in range(min(x0,x1) + 1, max(x0,x1)):
                    if (x,y0) in noKingFriendlyMoves:
                        return True

            if (x0 < x1 and y0 < y1 and x1-x0 > 1):
                for d in range(1,x1-x0):
                    if (x0+d,y0+d) in noKingFriendlyMoves:
                        return True

            if (x0 < x1 and y0 > y1 and x1-x0 > 1):
                for d in range(1,x1-x0):
                    if (x0+d,y1+d) in noKingFriendlyMoves:
                        return True

            if (x0 > x1 and y0 < y1 and x0-x1 > 1):
                for d in range(1,x0-x1):
                    if (x1+d,y0+d) in noKingFriendlyMoves:
                        return True

            if (x0 > x1 and y0 > y1 and x0-x1 > 1):
                for d in range(1,x0-x1):
                    if (x1+d,y1+d) in noKingFriendlyMoves:
                        return True
                
    return False

def getEnemyMoves(color, pieceDicts, withKing, capture):
    """compiles and returns all enemy possible moves into a set"""
    enemyMoves = set()
    checkingPieces = []
    for piece in pieceDicts[1-color].values():
        if ((piece.getType() == "king") and not withKing):
            continue
        for move in piece.getValidMoves(1-color, pieceDicts, True, capture):
            enemyMoves.add(move)
            if move == pieceDicts[color]["K"].getPos():
                checkingPieces.append(piece)
    return enemyMoves, checkingPieces
    
def isChecked(currentColor, pieceDicts): # is it checked?
    """determines if the king is being checked"""

    enemyMoves, checkingPieces = getEnemyMoves(currentColor,pieceDicts,True,True)
    if pieceDicts[currentColor]["K"].getPos() in enemyMoves:
        return True                     # if king is on the enemy's possible moves list
    else:                               # it is checked
        return False

def convertToString(inputTuple):
    """converts a tuple such as (3,4) to a string such as 'C4'."""
    columnDictionary = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}
    outputString = columnDictionary[inputTuple[0]]+str(inputTuple[1])
    return outputString

def game(board):
    """runs a single game."""

    # initializes some variables 
    endOfGame = False
    currentColor = 0
    colorList = ["White", "Black"]
    previousMessage = ""

    # starts the game and board
    board.setGameStart("It is White's move.")
    pieceDicts = setupGame(colorList, board)
    
    while endOfGame == 0:
        endOfGame, previousMessage = move(board, currentColor,
                                          pieceDicts,
                                          previousMessage, colorList)
        currentColor = 1 - currentColor

    if endOfGame != 1:
        return True

    # activiate Play Again Button
    time.sleep(3)
    board.setGameEnd(colorList[currentColor] + " has won!")
    
    p = board.getWin().getMouse()
    while not (board.againButtonClicked(p) or board.quitButtonClicked(p)):
        p = board.getWin().getMouse()

    if board.getQuitStatus():
        return True
    else:
        # clear board
        for i in range(0, 2):
            for piece in pieceDicts[i].values():
                board.undrawPiece(convertToString(piece.getPos()))
                
        return False

def main():
    """supports multiple games."""
    board = ChessBoard()
    quitGame = False
    
    while not quitGame:
        quitGame = game(board)

    board.quitGame()
    
main()





















