import pygame

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_BUFFER = 10 # this is just distance between Wall and Paddle
BALL_WIDTH = 10
BALL_HEIGHT = 10
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2
WHITE = (255, 255, 255) #  ye RGB code hai
BLACK = (0, 0, 0) # RGB code ye black ka

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#thats how canvas type of thing is initialise
def drawBall(ballXPos, ballYPos):
    #small rectangle, create it
    ball = pygame.Rect(ballXPos, ballYPos, BALL_WIDTH, BALL_HEIGHT)
    #draw it
    pygame.draw.rect(screen, WHITE, ball)


def drawPaddle1(paddle1YPos):
    #crreate it
    paddle1 = pygame.Rect(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    #draw it
    pygame.draw.rect(screen, WHITE, paddle1)    

def drawPaddle2(paddle2YPos):
    #create it, opposite side
    paddle2 = pygame.Rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    #draw it
    pygame.draw.rect(screen, WHITE, paddle2)   