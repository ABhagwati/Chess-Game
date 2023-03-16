# Knight subclass

from graphics import *
from ChessBoardGUI import ChessBoard
from ChessPieces import *
class Knight(Piece):

    """Each Knight will start at their given loccation and move
    according to where the user wants it to move. It can only move in an
    L-shape (Ex: 2 spaces up then 1 right or 1 left then 2 spaces up)."""

    def getValidMoves(self,currentColor,pieceDicts, protection, capture):
        validMoves = []
        coordsList = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)] # all the spaces the knight can move from its position

        for coords in coordsList:
            occupied = False
            x,y = self.column + coords[0], self.row + coords[1]
            if (x in range(1,9) and y in range(1,9)):
                if not protection:
                    for friendly in pieceDicts[currentColor].values():
                        if friendly.getPos() == (x,y):
                            occupied = True # space is occupied and move is not possible
                            break

                if not occupied: 
                    validMoves.append((x,y)) # space is not occupied and move is possible
                 
        return validMoves

    # this method was not used in the game but we wrote it initially and then realized we messed up since we used different coordinate systems
    def PossibleMoves(self, pos, friendlySquares):
        "Checks what moved the knight is allowed to make."
##        pos_x = super.getX(self)
##        pos_y = super.getY(self)
        possibleSquares = []
        friendlySquares = friendlySquares
        
        if self.color == "white":
            for element in self.board:
                # forwards
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] + 1)) and (int(element[1]) == int(self.row) + 2):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] - 1)) and (int(element[1]) == int(self.row) + 2):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] + 2)) and (int(element[1]) == int(self.row) + 1):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] - 2)) and (int(element[1]) == int(self.row) + 1):
                    possibleSquares.append(element)
                # backwards
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] + 1)) and (int(element[1]) == int(self.row) - 2):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] - 1)) and (int(element[1]) == int(self.row) - 2):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] + 2)) and (int(element[1]) == int(self.row) - 1):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] - 2)) and (int(element[1]) == int(self.row) - 1):
                    possibleSquares.append(element)

                for ele in friendlySquares:
                    if ele == element:
                        possibleSquares.remove(element)
                
        if self.color == "black":
            for element in self.board:
                # backwards
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] + 1)) and (int(element[1]) == int(self.row) + 2):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] - 1)) and (int(element[1] == int(self.row) + 2)):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] + 2)) and (int(element[1] == int(self.row) + 1)):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] - 2)) and (int(element[1] == int(self.row) + 1)):
                    possibleSquares.append(element)
                # forwards
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] + 1)) and (int(element[1] == int(self.row) - 2)):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] - 1)) and (int(element[1] == int(self.row) - 2)):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] + 2)) and (int(element[1] == int(self.row) - 1)):
                    possibleSquares.append(element)
                if (self.columnDictionary[element[0]] == (self.columnDictionary[self.column] - 2)) and (int(element[1] == int(self.row) - 1)):
                    possibleSquares.append(element)

                for ele in friendlySquares:
                    if ele == element:
                        possibleSquares.remove(element)

        return possibleSquares
