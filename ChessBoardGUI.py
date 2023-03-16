# Chess Board Class

from graphics import *
from Button2 import Button
from Button1 import ButtonOne
##from ChessPieces import *


class ChessBoard:
    """Draws the GUI on which the chess game can be played.
    The squares on the chess board are buttons that the user
    clicks on to move the pieces. Also has buttons for starting
    and quitting the game."""

    def __init__(self):
        self.win = GraphWin("Chess Board",950,950)
        # setting coordinates
        self.win.setCoords(-1,-1,14,17)
        self.quit = False
        self.imageDict = {}

        self.msgBox = Text(Point(5.5,15), '')

        # drawing the squares on the board as buttons in the form of a dictionary
        self.squares = {'A1':Button(self.win,Point(1,1),1.5,1.5,"brown4"),
        'A2':Button(self.win,Point(1,2.5),1.5,1.5,"ghost white"),
        'A3':Button(self.win,Point(1,4),1.5,1.5,"brown4"),
        'A4':Button(self.win,Point(1,5.5),1.5,1.5,"ghost white"),
        'A5':Button(self.win,Point(1,7),1.5,1.5,"brown4"),
        'A6':Button(self.win,Point(1,8.5),1.5,1.5,"ghost white"),
        'A7':Button(self.win,Point(1,10),1.5,1.5,"brown4"),
        'A8':Button(self.win,Point(1,11.5),1.5,1.5,"ghost white"),
        'B1':Button(self.win,Point(2.5,1.0),1.5,1.5,"ghost white"),
        'B2':Button(self.win,Point(2.5,2.5),1.5,1.5,"brown4"),
        'B3':Button(self.win,Point(2.5,4),1.5,1.5,"ghost white"),
        'B4':Button(self.win,Point(2.5,5.5),1.5,1.5,"brown4"),
        'B5':Button(self.win,Point(2.5,7),1.5,1.5,"ghost white"),
        'B6':Button(self.win,Point(2.5,8.5),1.5,1.5,"brown4"),
        'B7':Button(self.win,Point(2.5,10),1.5,1.5,"ghost white"),
        'B8':Button(self.win,Point(2.5,11.5),1.5,1.5,"brown4"),
        'C1':Button(self.win,Point(4,1),1.5,1.5,"brown4"),
        'C2':Button(self.win,Point(4,2.5),1.5,1.5,"ghost white"),
        'C3':Button(self.win,Point(4,4),1.5,1.5,"brown4"),
        'C4':Button(self.win,Point(4,5.5),1.5,1.5,"ghost white"),
        'C5':Button(self.win,Point(4,7),1.5,1.5,"brown4"),
        'C6':Button(self.win,Point(4,8.5),1.5,1.5,"ghost white"),
        'C7':Button(self.win,Point(4,10),1.5,1.5,"brown4"),
        'C8':Button(self.win,Point(4,11.5),1.5,1.5,"ghost white"),
        'D1':Button(self.win,Point(5.5,1),1.5,1.5,"ghost white"),
        'D2':Button(self.win,Point(5.5,2.5),1.5,1.5,"brown4"),
        'D3':Button(self.win,Point(5.5,4),1.5,1.5,"ghost white"),
        'D4':Button(self.win,Point(5.5,5.5),1.5,1.5,"brown4"),
        'D5':Button(self.win,Point(5.5,7),1.5,1.5,"ghost white"),
        'D6':Button(self.win,Point(5.5,8.5),1.5,1.5,"brown4"),
        'D7':Button(self.win,Point(5.5,10),1.5,1.5,"ghost white"),
        'D8':Button(self.win,Point(5.5,11.5),1.5,1.5,"brown4"),
        'E1':Button(self.win,Point(7,1),1.5,1.5,"brown4"),
        'E2':Button(self.win,Point(7,2.5),1.5,1.5,"ghost white"),
        'E3':Button(self.win,Point(7,4),1.5,1.5,"brown4"),
        'E4':Button(self.win,Point(7,5.5),1.5,1.5,"ghost white"),
        'E5':Button(self.win,Point(7,7),1.5,1.5,"brown4"),
        'E6':Button(self.win,Point(7,8.5),1.5,1.5,"ghost white"),
        'E7':Button(self.win,Point(7,10),1.5,1.5,"brown4"),
        'E8':Button(self.win,Point(7,11.5),1.5,1.5,"ghost white"),
        'F1':Button(self.win,Point(8.5,1),1.5,1.5,"ghost white"),
        'F2':Button(self.win,Point(8.5,2.5),1.5,1.5,"brown4"),
        'F3':Button(self.win,Point(8.5,4),1.5,1.5,"ghost white"),
        'F4':Button(self.win,Point(8.5,5.5),1.5,1.5,"brown4"),
        'F5':Button(self.win,Point(8.5,7),1.5,1.5,"ghost white"),
        'F6':Button(self.win,Point(8.5,8.5),1.5,1.5,"brown4"),
        'F7':Button(self.win,Point(8.5,10),1.5,1.5,"ghost white"),
        'F8':Button(self.win,Point(8.5,11.5),1.5,1.5,"brown4"),
        'G1':Button(self.win,Point(10,1),1.5,1.5,"brown4"),
        'G2':Button(self.win,Point(10,2.5),1.5,1.5,"ghost white"),
        'G3':Button(self.win,Point(10,4),1.5,1.5,"brown4"),
        'G4':Button(self.win,Point(10,5.5),1.5,1.5,"ghost white"),
        'G5':Button(self.win,Point(10,7),1.5,1.5,"brown4"),
        'G6':Button(self.win,Point(10,8.5),1.5,1.5,"ghost white"),
        'G7':Button(self.win,Point(10,10),1.5,1.5,"brown4"),
        'G8':Button(self.win,Point(10,11.5),1.5,1.5,"ghost white"),
        'H1':Button(self.win,Point(11.5,1),1.5,1.5,"ghost white"),
        'H2':Button(self.win,Point(11.5,2.5),1.5,1.5,"brown4"),
        'H3':Button(self.win,Point(11.5,4),1.5,1.5,"ghost white"),
        'H4':Button(self.win,Point(11.5,5.5),1.5,1.5,"brown4"),
        'H5':Button(self.win,Point(11.5,7),1.5,1.5,"ghost white"),
        'H6':Button(self.win,Point(11.5,8.5),1.5,1.5,"brown4"),
        'H7':Button(self.win,Point(11.5,10),1.5,1.5,"ghost white"),
        'H8':Button(self.win,Point(11.5,11.5),1.5,1.5,"brown4")}
        # column designations
        Text(Point(0,1), "1").draw(self.win).setSize(18)
        Text(Point(0,2.5), "2").draw(self.win).setSize(18)
        Text(Point(0,4), "3").draw(self.win).setSize(18)
        Text(Point(0,5.5), "4").draw(self.win).setSize(18)
        Text(Point(0,7), "5").draw(self.win).setSize(18)
        Text(Point(0,8.5), "6").draw(self.win).setSize(18)
        Text(Point(0,10), "7").draw(self.win).setSize(18)
        Text(Point(0,11.5), "8").draw(self.win).setSize(18)
        Text(Point(12.5,1), "1").draw(self.win).setSize(18)
        Text(Point(12.5,2.5), "2").draw(self.win).setSize(18)
        Text(Point(12.5,4), "3").draw(self.win).setSize(18)
        Text(Point(12.5,5.5), "4").draw(self.win).setSize(18)
        Text(Point(12.5,7), "5").draw(self.win).setSize(18)
        Text(Point(12.5,8.5), "6").draw(self.win).setSize(18)
        Text(Point(12.5,10), "7").draw(self.win).setSize(18)
        Text(Point(12.5,11.5), "8").draw(self.win).setSize(18)
        # row designations
        Text(Point(1,12.5), "a").draw(self.win).setSize(18)
        Text(Point(2.5,12.5), "b").draw(self.win).setSize(18)
        Text(Point(4,12.5), "c").draw(self.win).setSize(18)
        Text(Point(5.5,12.5), "d").draw(self.win).setSize(18)
        Text(Point(7,12.5), "e").draw(self.win).setSize(18)
        Text(Point(8.5,12.5), "f").draw(self.win).setSize(18)
        Text(Point(10,12.5), "g").draw(self.win).setSize(18)
        Text(Point(11.5,12.5), "h").draw(self.win).setSize(18)
        Text(Point(1,0), "a").draw(self.win).setSize(18)
        Text(Point(2.5,0), "b").draw(self.win).setSize(18)
        Text(Point(4,0), "c").draw(self.win).setSize(18)
        Text(Point(5.5,0), "d").draw(self.win).setSize(18)
        Text(Point(7,0), "e").draw(self.win).setSize(18)
        Text(Point(8.5,0), "f").draw(self.win).setSize(18)
        Text(Point(10,0), "g").draw(self.win).setSize(18)
        Text(Point(11.5,0), "h").draw(self.win).setSize(18)

        # Quit Button
        self.quitButton = ButtonOne(self.win,Point(11.5,15),2,1.5,"Quit")

        # Play Again Button
        self.againButton = ButtonOne(self.win,Point(1,15),2,1.5,"Play Again")

    def getWin(self):
        "Returns the window of the GUI."
        return self.win

    def setGameStart(self, message):
        "Sets the starting conditions of the GUI."
        self.msgBox.undraw()
        self.msgBox = Text(Point(5.5,15), message)
        self.msgBox.draw(self.win)
        self.quitButton.activate()
        self.againButton.deactivate()
        self.quit = False

    def setGameEnd(self, message):
        "Sets the ending conditions of the GUI."
        self.msgBox.undraw()
        self.msgBox = Text(Point(5.5,15), message)
        self.msgBox.draw(self.win)
        self.againButton.activate()

    def printMsg(self, message):
        "Print messages to the GUI."
        self.msgBox.undraw()
        self.msgBox = Text(Point(5.5,15), message)
        self.msgBox.draw(self.win)
        print(message)
        # return self.msgBox

    def AssociateStrings(self, Squares): # takes in list of squares (Ex: ['A1','F2','G3'])
        "Associates square strings to the actual sqaures on the board."
        associated_squares = []
        for square in Squares:
            associated_squares.append(self.squares[square])

        return associated_squares

    def SquareX(self, pos):
        "Gets X-coordinate of the square."
        x_value = self.squares[pos].getX()
        return x_value
    def SquareY(self, pos):
        "Gets Y-coordinate of the square."
        y_value = self.squares[pos].getY()
        return y_value
            
    def quitGame(self):
        "Quits the game and closes the GUI."
        self.printMsg("Quit Game")
        self.win.close()
        sys.exit()

    def getClickedSquare(self, p):
        "Returns the square that was clicked on the board."
##        for sq in self.squares:
##            actual_sq = self.squares.get(sq)
##            if actual_sq.clicked(p) == True:
##                return sq.getPos()
        posX = round(self.p2pos(p.getX()))
        posY = round(self.p2pos(p.getY()))
        return (posX,posY)
            
    def isClickOn8x8(self, p):
        "Determines if the user clicked on the board or not; returns True or False."
        if (p.getX() >= 0.25 and p.getX() <= 12.25) and (p.getY() >= 0.25 and p.getY() <= 12.25):
            return True
        else:
            return False

    def drawPiece(self, piece_pos, image):
        "Draws piece/image on the board based on its position."
        x = self.pos2p(piece_pos[0])
        y = self.pos2p(piece_pos[1])
        image = Image(Point(x, y), image)
        self.imageDict[(x, y)] = image
        image.draw(self.win)

    def p2pos(self, p):
        return (p + 0.5) / 1.5

    def pos2p(self, pos):
        return (pos * 1.5 - 0.5)

    def undrawPiece(self, posString):
        "Undraw piece/image from the board."
        x = self.squares[posString].getX()
        y = self.squares[posString].getY()
        self.imageDict[(x, y)].undraw()
        
    def quitButtonClicked(self, p):
        "Quit button is clicked."
##        print(p.getX())
##        print(p.getY())
        if (p.getX() >= 10.5 and p.getX() <= 12.5) and (p.getY() >= 14.25 and p.getY() <= 15.75):
            self.quit = True
            return True
        else:
            return False

    def againButtonClicked(self, p):
        "Play again button is clicked."
##        print(p.getX())
##        print(p.getY())
        if (p.getX() >= 0 and p.getX() <= 2) and (p.getY() >= 14.25 and p.getY() <= 15.75):
            return True
        else:
            return False
        
    def getQuitStatus(self):
        "Returns if self.quit is True or False."
        return self.quit

    def highlight(self, posString):
        "Accesses button class to highlight the squares."
        Button=self.squares[posString]
        Button.highlight()

    def unhighlight(self, posString):
        "Accesses button class to unhighlight the squares."
        Button=self.squares[posString]
        Button.unhighlight()
