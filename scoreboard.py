print("GFG")
from turtle import Turtle
 #save the highest score you get
try:
    score = int(open('highestScore.txt', 'r').read())
except FileNotFoundError:
    score = open('highestScore.txt', 'w').write(str(0))
except ValueError:
    score = 0
FONT = ('Courier', 16, 'normal')
#display score, lives, and highestscore
class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color('gray')
        self.penup()
        self.hideturtle()
        self.highScore = score
        self.goto(x = -580, y = 260)
        self.lives = lives
        self.score = 0
        self.updateScore()
 
    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest Score: {self.highScore} | Lives: {self.lives}", align = 'left',
        font = FONT)
 #break bricks score increases
    def increaseScore(self):
        self.score += 1
        if self.score > self.highScore:
            self.highScore += 1
        self.updateScore()
 #when you die
 
    def decreaseLives(self):
        self.lives -= 1
        self.updateScore()
 #reset game and play again if you die or win
    def reset(self):
        self.clear()
        self.score = 0
        self.updateScore()
        open('highestScore.txt', 'w').write(str(self.highScore))