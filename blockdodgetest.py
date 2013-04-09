import pygame, sys
from pygame.locals import *
from random import randrange
FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
DARKGREEN = ( 0, 155, 0)
DARKGRAY = ( 40, 40, 40)
blockImg = pygame.image.load('box.png')


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.FONT('freesansbold.ttf', 18)
    pygame.display.set_caption('Blockdodge')
    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def runGame():
    xcoord = WINDOWWIDTH/2
    blockCoords = (xcoord, 20)
    spike = (randrange(0,WINDOWWIDTH),WINDOWHEIGHT)
    while TRUE: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT and xcoord-10>0):
                    xcoord-=10
                elif (event.key == K_RIGHT and xcoord+10<WINDOWWIDTH):
                    xcoord+=10
                elif event.key == K_ESCAPE:
                    terminate()

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, 
DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
 
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Block Dodge!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Block Dodge!', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(WHITE)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
    
        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)
    
        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degrees2 += 7
