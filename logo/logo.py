from Tkinter import *
from math import *

c = Canvas(width = 400, height = 400)
c.pack()

class Turtle():
    """This is a mini implimentation of LOGO in Python.
       Includes two methods, forward() to move the turtle a steps in the current direction
       and rotate_turtle() to rotate the turtle in the given angle
    """

    def __init__(self, c, x = 200, y = 200, angle = 0):
        self.x = x
	self.y = y
	self.angle = angle
	self.c = c
	self.a = c.create_polygon(215,200,200,195,200,205)
	self.pen = 1

    def forward(self, a):
	x1 = self.x + a * cos((self.angle / 180.00) * 3.14)
	y1 = self.y - a * sin((self.angle / 180.00) * 3.14)
	if self.pen:
	    self.c.create_line(self.x, self.y, x1, y1)
	self.x = x1
	self.y = y1
	self.c.move(self.a, a * cos((self.angle / 180.00) * 3.14), -(a * sin((self.angle / 180.00) * 3.14)))

    def rotate_turtle(self, angle):
	self.angle = self.angle + angle
	t.recreate_turtle()

    def recreate_turtle(self):
        self.c.delete(self.a)
	x1 = self.x + 15 * cos((self.angle / 180.00) * 3.14)
	y1 = self.y - 15 * sin((self.angle / 180.00) * 3.14)
	x2 = self.x + 5 * cos(((90 + self.angle) / 180.00) * 3.14)
	y2 = self.y - 5 * sin(((90 + self.angle) / 180.00) * 3.14)
	x3 = self.x + 5 * cos(((270 + self.angle) / 180.00) * 3.14)
	y3 = self.y - 5 * sin(((270 + self.angle) / 180.00) * 3.14)
	self.a = self.c.create_polygon(x1, y1, x2, y2, x3, y3)

    def hide(self):
	self.c.delete(self.a)

    def show(self):
	t.recreate_turtle()

    def pen_up(self):
	self.pen = 0

    def pen_down(self):
	self.pen = 1

    

t = Turtle(c)
