from turtle import Turtle
 
 
distancemove = 70
 
#constructing shape and movements of the paddle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 10)
        self.goto(x = 0, y = -280)
 
    def moveLeft(self):
        self.backward(distancemove)
 
    def moveRight(self):
        self.forward(distancemove)