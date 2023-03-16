from graphics import *

#takes in 5 parameters: window, center, width, height, and label
#creates a rectangle given the center, width, and height
#will label the button through the parameter that is passed
#all my buttons are lightSkyBlue1 because it's a nice color that stands out
class ButtonOne:
    '''Button class: activates/deactivates, sets labels, clicks.'''
    def __init__(self,win,center,width,height,label):
        self.win = win
        self.centerX = center.getX()
        self.centerY = center.getY()
        self.width= width
        self.height = height
        self.label = Text(center, label)
        self.active = True

        self.p1x = self.centerX - self.width/2
        self.p2x = self.centerX + self.width/2
        self.p1y = self.centerY - self.height/2
        self.p2y = self.centerY + self.height/2
        self.button = Rectangle(Point(self.p1x, self.p1y), Point(self.p2x, self.p2y))
        self.button.setFill("lightSkyBlue1")
        self.button.draw(self.win)
        self.label.draw(self.win)

    def activate(self):
        '''This activates the button, allowing it to be clicked.'''
        self.active = True
        self.button.setFill("lightSkyBlue1")

    def deactivate(self):
        '''This deactivates the button, disabling clicking.'''
        self.active = False
        self.button.setFill("DarkGrey")

    def clicked(self, pt):
        '''This checks if the point that is passed is inside the button, and if it is, it returns true.'''
        #checks if the x is between the x endpoints and y is between the y endpoints of the rectangle
        if self.p1x <= pt.getX() <= self.p2x and self.p1y <= pt.getY() <= self.p2y:
            return True


