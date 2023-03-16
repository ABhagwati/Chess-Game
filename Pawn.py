# Pawn subclass

from ChessPieces import Piece


class Pawn(Piece):
    """defines Pawn class."""

    def getValidMoves(self, currentColor, pieceDicts, protection, capture):
        """returns all valid moves based on piece config and pawn pos"""
        validMoves = []
        
        if currentColor == 1:       # decides possible move list based on color and capture
            if self.moved:          # and if moved
                moveList = [(0,-1)]
            else:
                moveList = [(0,-2),(0,-1)]
            captureList = [(1,-1),(-1,-1)]
            
        else:
            if self.moved:
                moveList = [(0,1)]
            else:
                moveList = [(0,2),(0,1)]
            captureList = [(1,1),(-1,1)]
            
        if not capture:             # if no capture, only go straight
            for coords in moveList:
                occupied = False
                x,y = self.column + coords[0], self.row + coords[1]
                if (x in range(1,9) and y in range(1,9)):
                    for friendly in pieceDicts[currentColor].values():
                        if friendly.getPos() == (x,y):
                            occupied = True
                            break
                        
                    if not occupied:
                        for enemy in pieceDicts[1-currentColor].values():
                            if enemy.getPos() == (x,y):
                                occupied = True
                                break
                        
                        if not occupied:
                            validMoves.append((x,y))
                        
        for coords in captureList:
            occupied = False
            x,y = self.column + coords[0], self.row + coords[1]
            if (x in range(1,9) and y in range(1,9)):
                if not capture:
                    for friendly in pieceDicts[1-currentColor].values():
                        if friendly.getPos() == (x,y):
                            occupied = True
                            break
                        
                if capture or occupied:
                    validMoves.append((x,y))
            
        return validMoves

    def makeMove(self, newPos):
        """sets position to new position"""
        self.setPos(newPos)
        if ((self.color == "White" and self.row == 8) or (self.color == "Black" and self.row == 1)):
            self.promoted = True

        
