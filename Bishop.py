# Bishop subclass

from graphics import *
from ChessBoardGUI import ChessBoard
from ChessPieces import *

class Bishop(Piece):

    """Each Bishop will start at their given loation and move
    according to where the user wants it to move. It can only
    move in a diagonal direction."""

    def getValidMoves(self,currentColor,pieceDicts, protection, capture):
        validMoves = self.diagonalGen(currentColor, pieceDicts, protection) # using the diagonal system that was made in piece super class

        return validMoves

    # this method was not used in the game but we wrote it initially and then realized we messed up since we used different coordinate systems
    def PossibleMoves(self, pos, enemySquares, friendlySquares):
        "Checks what moves the bishop is allowed to make."
##        pos_x = super.getX(self)
##        pos_y = super.getY(self)
        possibleSquares = []
        friendlySquares = friendlySquares
        enemySquares = enemySquares
        occupiedSquares = friendlySquares + enemySquares

        break_loop = False

        if self.color == "white":
            for element in self.board:
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 1) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 1)) and (int(element[1]) == int(self.row) + 1):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 2) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 2)) and (int(element[1]) == int(self.row) + 2):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 3) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 3)) and (int(element[1]) == int(self.row) + 3):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 4) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 4)) and (int(element[1]) == int(self.row) + 4):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 5) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 5)) and (int(element[1]) == int(self.row) + 5):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 6) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 6)) and (int(element[1]) == int(self.row) + 6):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 7) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 7)) and (int(element[1]) == int(self.row) + 7):
                    possibleSquares.appened(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 8) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 8)) and (int(element[1]) == int(self.row) + 8):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break

            for square in enemySquares:
                possibleSquares.append(square)
        
            

        if self.color == "black":
            for element in self.board:
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 1) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 1)) and (int(element[1]) == int(self.row) - 1):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 2) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 2)) and (int(element[1]) == int(self.row) - 2):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 3) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 3)) and (int(element[1]) == int(self.row) - 3):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 4) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 4)) and (int(element[1]) == int(self.row) - 4):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 5) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 5)) and (int(element[1]) == int(self.row) - 5):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 6) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 6)) and (int(element[1]) == int(self.row) - 6):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 7) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 7)) and (int(element[1]) == int(self.row) - 7):
                    possibleSquares.appened(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break
                if ((self.columnDictionary[element[0]] == self.columnDictionary[self.column] + 8) or (self.columnDictionary[element[0]] == self.columnDictionary[self.column] - 8)) and (int(element[1]) == int(self.row) - 8):
                    possibleSquares.append(element)
                if len(possibleSquares) > 0:
                    for square in possibleSquares:
                        for ele in occupiedSquares:
                            if square == ele:
                                possibleSquares.remove(square)
                                break_loop = True
                if break_loop == True:
                    break

            for square in enemySquares:
                possibleSquares.append(square)
        
            

        return possibleSquares               
                        

        
                    
