from turtle import Turtle, distance
 
distance = 10
 
#constructing the turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('black')
        self.penup()
        self.xmoveDist = distance
        self.ymoveDist = distance
        self.reset()
#moves off of the paddle
    def move(self):
        new_y = self.ycor() + self.ymoveDist
        new_x = self.xcor() + self.xmoveDist
        self.goto(x = new_x, y = new_y)
#angles and how it bounces from wall
    def bounce(self, xBounce, yBounce):
        if xBounce:
            self.xmoveDist *= -1
 
        if yBounce:
            self.ymoveDist *= -1
#die and it resets
    def reset(self):
        self.goto(x = 0, y = -240)
        self.ymoveDist = 10
    