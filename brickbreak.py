#2022 FALL
#CS212
#PRACTICAL PYTHON
#P-02
#GAME PROJECT
#VERSION 3
#WEDNESDAY, 14 DECEMBER 2022
#MEGHAN NULF

#IN MY CODE I HAVE 6 DIFFERENT FILES WITH CLASSES THAT CONSTRUCT EACH PART OF THE GAME
#THEN IN MY MAIN I MADE PARAMETERS FOR EACH RULE WITHIN WHAT HAPPENS IF THE BALL HITS THE WALL, BRICKS,
#OR IT HITS THE PADDLE
#I MADE A SCOREBOARD AS WELL AS AN EXTRA FILE THAT KEEPS TRACK OF YOUR HIGHEST SCORE INDEFINITELY
#I USED TIME AS WELL AS RANDOM TO CHOOSE COLORS AND OTHER RANDOMIZING NEEDING FUNCTIONS WITHIN THE GAME
#I AM THEN IMPLEMENTING TURTLE TO MAKE THE GAME COHESIVE AS WELL AS HOW IT WILL WORK IN THE FUTURE
#THE GAME RUNS SMOOTHLY, AND I HAVE SIMPLIFIED MY CODE AS WELL AS CHANGED THE AMOUNT OF BRICKS TO MAKE IT A QUICKEY
#GAME AND RUN SMOOTHER ON THE ENVIRONMNET YOU RUN IT ON.  I WATCHED VIDEOS AND OTHER TUTORIALS TO LEARN PERAMETERS AS I WAS
#CONFUSED ON HOW TO MAKE IT WORK, BUT I DO BELIVE I CODED THIS CORRECTLY WITHIN THE PARAMETERS OF THE PROJECT.  WHEN 
#I PRESENTED IN CLASS THAT WAS THE BETA VERSION, AND NOW I HAVE A SMOOTH RUNNING GAME.  


import turtle as Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from ui import UI
from bricks import Bricks
import time


screen = Turtle.Screen()
screen.setup(width = 1200, height = 600)
screen.bgcolor("white")
screen.title('Breakout!')
screen.tracer(0)

#game screen
ui = UI()
ui.header()

#initializing the game componenets
score = Scoreboard(lives = 5)
paddle = Paddle()
bricks = Bricks()
ball = Ball()


playing_Game = True

#pause definition
 
#code to take user instructions
screen.listen()
screen.onkey(key = 'Left', fun = paddle.moveLeft)
screen.onkey(key = 'Right', fun = paddle.moveRight)


def wallCollision():
    global ball, score, playing_Game, ui
    #collision with left and right ball
    if ball.xcor() < -580  or ball.xcor() > 570:
        ball.bounce(xBounce = True, yBounce = False)
        return
    
    #upper wall collisino
    if ball.ycor() > 270:
        ball.bounce(xBounce = False, yBounce = True)
        return
    
    #collision with bottom wall
    if ball.ycor() < -280:
        ball.reset()
        score.decreaseLives()
        if score.lives == 0:
            score.reset()
            playing_Game = False
            ui.gameOver(win = False)
            return
        ui.changeColor()
        return
    
def paddleCollision():
    global ball, paddle
    #x coordinates of ball and paddle
    paddleX = paddle.xcor()
    ballX = ball.xcor()
 
    # ball distance check to see if it is less then paddle width and below coordinate to check collision
    if ball.distance(paddle) < 110 and ball.ycor() < -250:
 
        #Paddle is on Right of Screen
        if paddleX > 0:
            if ballX > paddleX:
                # hit ball left go back to left
                ball.bounce(xBounce = True, yBounce = True)
                return
            else:
                ball.bounce(xBounce = False, yBounce = True)
                return
 
        #Paddle is left of Screen
        elif paddleX < 0:
            if ballX < paddleX:
                # hits left side it goes backleft side
                ball.bounce(xBounce = True, yBounce = True)
                return
            else:
                ball.bounce(xBounce = False, yBounce = True)
                return
 
        # paddle bounce straight up
        else:
            if ballX > paddleX:
                ball.bounce(xBounce = True, yBounce = True)
                return
            elif ballX < paddleX:
                ball.bounce(xBounce = True, yBounce = True)
                return
            else:
                ball.bounce(xBounce = False, yBounce = True)
                return
            
def brickCollision():
    global ball, bricks, score
    for brick in bricks.bricks:
#add to a score if a brick dissapears and then subrtact it from total count once you break it
        if ball.distance(brick) < 40:
            score.increaseScore()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)
 
            # left collision
            if ball.xcor() < brick.leftWall: 
                ball.bounce(xBounce = True, yBounce = False)
 
            #right collision
            elif ball.xcor() > brick.rightWall:
                ball.bounce(xBounce = True, yBounce = False)
 
            #bottom collision
            elif ball.ycor() < brick.bottomWall:
                ball.bounce(xBounce = False, yBounce = True)
 
            #top collision
            elif ball.ycor() > brick.upperWall:
                ball.bounce(xBounce = False, yBounce = True)
 
#pull everything together to make the game run
while playing_Game:
        screen.update()
        time.sleep(0.02)
        ball.move()
        
        wallCollision()
        paddleCollision()
        brickCollision()
        
        if len(bricks.bricks) == 0:
            ui.gameOver(win = True)
            break

Turtle.mainloop()