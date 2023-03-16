# Queen subclass

from ChessPieces import Piece



class Queen(Piece):
     """Each queen will start at their given loccation and move
     according to where the user wants it to move. It only move straight
     or diagonally."""

     def getValidMoves(self, currentColor, pieceDicts, protection, capture):
        """determines possible moves based on straight and diagonal gen."""
        diagonal = self.diagonalGen(currentColor, pieceDicts, protection)
        straight = self.straightGen(currentColor, pieceDicts, protection)

        validMoves = diagonal + straight

        return validMoves
        
