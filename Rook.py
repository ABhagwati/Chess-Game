# Rook subclass

from ChessPieces import Piece

class Rook(Piece):
     """Each rook will start at their given loccation and move
     according to where the user wants it to move. It can only move
     in straight lines."""

     def getValidMoves(self,currentColor,pieceDicts, protection, capture):
        """uses straight generation to find valid moves."""
        validMoves = self.straightGen(currentColor, pieceDicts, protection)

        return validMoves
