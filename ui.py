import time
from turtle import Turtle
import random
 
font = ("Arial", 42, "normal")
font2 = ("Arial", 22, "normal")
placement = 'center'
color = "gray"
#to make title "breakout" be random and multicolored
colorList = ['blue', 'yellow',
              'green', 'orange',
              'red', 'indigo',
              'violet', 'salmon', 'maroon',
              'brown', 'purple', 'deep pink',
              'sea green', 'dark grey']
 
 
class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(colorList))
        self.header()
 #how breakout is written on screen
    def header(self):
        self.clear()
        self.goto(x = 0, y = -150)
        self.write('Breakout', align = placement, font = font)
        self.goto(x = 0, y = -180)
 
    def changeColor(self):
        self.clear()
        self.color(random.choice(colorList))
        self.header()
 
    def gameOver(self, win):
        self.clear()
        if win == True:
            self.write('You win!', align = 'center', font = font)
        else:
            self.write("You lost", align = 'center', font = font)