# King subclass

from ChessPieces import Piece
    

class King(Piece):
    """Each King will start at their given loccation and move
    according to where the user wants it to move. It can only move 1
    square in each dir."""

    def getValidMoves(self,currentColor,pieceDicts, protection, capture):
        """determines valid moves."""
        validMoves = []
        coordsList = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

        for coords in coordsList:
            occupied = False
            x,y = self.column + coords[0], self.row + coords[1]
            if (x in range(1,9) and y in range(1,9)):
                if not protection:
                    for friendly in pieceDicts[currentColor].values():
                        if friendly.getPos() == (x,y):
                            occupied = True
                            break

                if not occupied:
                    validMoves.append((x,y))

        return validMoves
