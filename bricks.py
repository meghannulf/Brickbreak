from turtle import Turtle
import random
 #colors!!
colorList = ['blue', 'yellow',
              'green', 'orange',
              'red', 'indigo',
              'violet', 'salmon', 'maroon',
              'brown', 'purple', 'deep pink',
              'sea green', 'dark grey']
#how many times the bricks get hit before dissapearing
weights = [1, 2, 1, 1, 3, 2, 1, 4, 1,
           3, 1, 1, 1, 4, 1, 3, 2, 2,
           1, 2, 1, 2, 1, 2, 1]
 
#constructed shapes from turtle
class Brick(Turtle):
    def __init__(self, x_Cor, y_Cor):
        super().__init__()
        self.penup()
        self.shape('square')
        #constructor of each brick
        self.shapesize(stretch_wid = 1.5, stretch_len = 3.5)
        self.color(random.choice(colorList))
        self.goto(x = x_Cor, y = y_Cor)
 
        self.quantity = random.choice(weights)
 
        # Defining borders of the brick
        self.leftWall = self.xcor() - 30
        self.rightWall = self.xcor() + 30
        self.upperWall = self.ycor() + 15
        self.bottomWall = self.ycor() - 15
 
#class to randomize and set brick rows
class Bricks:
    def __init__(self):
        self.yStart = 80
        self.yEnd = 240
        self.bricks = []
        self.createLanes()
 #make one lane
    def createLane(self, y_Cor):
        for i in range(-570, 570, 63):
            brick = Brick(i, y_Cor)
            self.bricks.append(brick)
 #to make howver many lanes fit within the given confinements
    def createLanes(self):
        for i in range(self.yStart, self.yEnd, 32):
            self.createLane(i)