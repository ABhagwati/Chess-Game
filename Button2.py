#
# Name: Arav Bhagwati
# Creating a button class

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    return true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, color):
        """Creates a rectangular button, eg:
        qb = Button(myWin, CenterPoint, width, height, 'Black') """

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1= Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.rect.draw(win)
        #self.deactivate()
        self.center = center
        self.color = color
        self.active = False #MJ

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

##    def getLabel(self):
##        "Returns the label string of this button."
##        return self.label.getText()

    def setLabel(self, new_label):
        "Changes label on button."
        self.label.setText(new_label)

    def activate(self):
        "Sets button to 'active'."
##        self.label.setFill('black')
##        self.rect.setFill(color)
        #self.rect.setWidth(5)
        self.active = True

    def deactivate(self):
##        "Sets this button to 'inactive'."
##        self.label.setFill('darkgrey')
##        self.rect.setFill('lightgray')
##        self.rect.setWidth(1)
        self.active = False

    def undraw(self):
        "Undraw the button."
        #self.label.undraw()
        self.rect.undraw()

    def setFill(self, color):
        "Sets color of button to any color"
        self.rect.setFill(color)

    def getX(self):
        return self.center.getX()

    def getY(self):
        return self.center.getY()

    def getPos(self):
        return self.center

    def highlight(self):
        self.rect.setFill('khaki1')

    def unhighlight(self):
        self.rect.setFill(self.color)

##    def setFill2(self, color):
##        "Sets color of label to any color"
##        self.label.setFill(color)
##
