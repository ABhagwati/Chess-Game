# chess piece classes
from graphics import*
from ChessBoardGUI import ChessBoard

class Piece:
    """a superclass that supports all pieces. Includes methods that
       all pieces can use."""
    
    def __init__(self, pos, color, piece_type, imageName):
        """initializes each piece with characteristics
           shared by all of them."""
        self.pos = pos
        self.column = pos[0]
        self.row = pos[1]
        self.color = color
##        self.isCurrentEnemy = False
        self.validMoves = []
        self.imageName = imageName
        self.type = piece_type
        self.moved = False
        self.promoted = False               # for pawn

    def checkIfMoved(self, pos):
        """determines if the piece has ever been moved."""
        return self.moved
        
    def setPos(self, pos):
        """sets a new position for a piece."""
        if pos != self.pos:
            self.moved = True
        self.pos = pos
        self.column = pos[0]
        self.row = pos[1]
        
    def getPos(self):
        """returns the position of a piece (tuple)."""
        return self.pos

    def getColor(self):
        """returns the color of a piece (string)."""
        return self.color

    def getImageName(self):
        """returns the image name of a piece (string)."""
        return self.imageName

    def getType(self):
        """returns the type of a piece (string)."""
        return self.type

    def makeMove(self, newPos):
        """sets the position of a piece."""
        self.setPos(newPos)

    def getPromoteStatus(self):
        """returns the promotion status of a piece.
           only for pawns"""
        return self.promoted

    def diagonalGen(self, currentColor, pieceDicts, protection):
        """generates diagonal moves (for bishop and queen)."""
        if self.type in ["bishop", "queen"]:
            yxDiff = self.row - self.column # some numerical values to facilitate
            yxSum = self.row + self.column  # writing and computation
            drmin = max(1 + yxDiff, 1)
            drmax = min(8 + yxDiff, 8)      # min/max: a way to shrink the range
            dfmin = max(yxSum - 8, 1)       # when a piece is closest to the selected
            dfmax = min(yxSum - 1, 8)
            if protection:                  # when protection is true, with addition
                buffer = 0                  # in addition to squares that are
            else:                           # controlled by the piece, it also covers
                buffer = 1                  # the other friendly pieces it reaches.
            for piece in pieceDicts[currentColor].values():
                
                if piece.getPos() == self.pos:
                    continue                # skip own piece
                                            # check own pieces, which will block range
                if (piece.getPos()[1] - piece.getPos()[0]) == yxDiff:
                    if (self.row < piece.getPos()[1] and piece.getPos()[1] <= drmax):
                        drmax = piece.getPos()[1] - buffer
                    if (self.row > piece.getPos()[1] and piece.getPos()[1] >= drmin):
                        drmin = piece.getPos()[1] + buffer
                        
                if (piece.getPos()[1] + piece.getPos()[0]) == yxSum:
                    if (self.row < piece.getPos()[1] and piece.getPos()[1] <= dfmax):
                        dfmax = piece.getPos()[1] - buffer
                    if (self.row > piece.getPos()[1] and piece.getPos()[1] >= dfmin):
                        dfmin = piece.getPos()[1] + buffer
                                            # check enemy pieces, which block but are capturable
            for piece in pieceDicts[1-currentColor].values():
                if (piece.getPos()[1] - piece.getPos()[0]) == yxDiff:
                    if (self.row < piece.getPos()[1] and piece.getPos()[1] <= drmax):
                        drmax = min(piece.getPos()[1], drmax)
                    if (self.row > piece.getPos()[1] and piece.getPos()[1] >= drmin):
                        drmin = max(piece.getPos()[1], drmin)
                        
                if (piece.getPos()[1] + piece.getPos()[0]) == yxSum:
                    if (self.row < piece.getPos()[1] and piece.getPos()[1] <= dfmax):
                        dfmax = min(piece.getPos()[1], dfmax)
                    if (self.row > piece.getPos()[1] and piece.getPos()[1] >= dfmin):
                        dfmin = max(piece.getPos()[1], dfmin)

            possibleMoves = []              # initialize possiblemoves
            
            for i in range(dfmin, dfmax + 1):
                if i != self.row:           # adds possible moves to the list
                    possibleMoves.append((yxSum-i,i))

            for i in range(drmin, drmax + 1):
                if i != self.row:           # adds possible moves to the list
                    possibleMoves.append((i-yxDiff,i))

            return possibleMoves

        else:
            return []            

    def straightGen(self, currentColor, pieceDicts, protection):
        """generates straight moves (for rook and for queen)."""
        if self.type in ["rook", "queen"]:
            ymin, ymax, xmin, xmax = 1,8,1,8
            if protection:                  # pretty much same as above, but
                buffer = 0                  # simpler because of the coordinates
            else:
                buffer = 1
            for piece in pieceDicts[currentColor].values():
                
                if piece.getPos() == self.pos:
                    continue
                                            # straight left/right friendlies
                if piece.getPos()[0] == self.column:
                    if (self.row < piece.getPos()[1] and piece.getPos()[1] <= ymax):
                        ymax = piece.getPos()[1] - buffer
                    if (self.row > piece.getPos()[1] and piece.getPos()[1] >= ymin):                    
                        ymin = piece.getPos()[1] + buffer
                                            # straight up/down friendlies
                if piece.getPos()[1] == self.row:
                    if (self.column < piece.getPos()[0] and piece.getPos()[0] <= xmax):
                        xmax = piece.getPos()[0] - buffer
                    if (self.column > piece.getPos()[0] and piece.getPos()[0] >= xmin):
                        xmin = piece.getPos()[0] + buffer
                        
            for piece in pieceDicts[1-currentColor].values():
                                            # straight left/right enemies
                if piece.getPos()[0] == self.column:
                    if (self.row < piece.getPos()[1] and piece.getPos()[1] <= ymax):
                        ymax = min(piece.getPos()[1], ymax)
                    if (self.row > piece.getPos()[1] and piece.getPos()[1] >= ymin):
                        ymin = max(piece.getPos()[1], ymin)
                                            # straight up/down enemies
                if piece.getPos()[1] == self.row:
                    if (self.column < piece.getPos()[0] and piece.getPos()[0] <= xmax):
                        xmax = min(piece.getPos()[0], xmax)
                    if (self.column > piece.getPos()[0] and piece.getPos()[0] >= xmin):
                        xmin = max(piece.getPos()[0], xmin)

            possibleMoves = []
            
            for i in range(xmin, xmax + 1):
                if i != self.column:
                    possibleMoves.append((i,self.row))
                                            # adds moves to list
            for i in range(ymin, ymax + 1):
                if i != self.row:
                    possibleMoves.append((self.column,i))

            return possibleMoves

        else:
            return []
