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
spikeImg = pygame.image.load('spike.png')

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Blockdodge')
    pygame.key.set_repeat(1, 10)
    
    #showStartScreen()
    while True:
        runGame()
        #showGameOverScreen()

def runGame():
    DISPLAYSURF.fill(WHITE)
    xcoord = WINDOWWIDTH/2
    spike1Coords = [randrange(0, WINDOWWIDTH), 0]
    spike2Coords = [randrange(0, WINDOWWIDTH), 0]
    while True: #main game loop
        DISPLAYSURF.fill(WHITE)
        #spike handling
        if spike1Coords[1] > WINDOWHEIGHT:
            spike1Coords = [randrange(0, WINDOWWIDTH), 0]
        else:
            spike1Coords[1]+=2
        if spike2Coords[1] > WINDOWHEIGHT:
            spike2Coords = [randrange(0, WINDOWWIDTH), 0]
        else:
            spike2Coords[1]+=3
        pygame.draw.polygon(DISPLAYSURF, BLACK, [spike1Coords, (spike1Coords[0]-10, spike1Coords[1]-20), (spike1Coords[0]+10, spike1Coords[1]-20)])
        pygame.draw.polygon(DISPLAYSURF, BLACK, [spike2Coords, (spike2Coords[0]-10, spike2Coords[1]-20), (spike2Coords[0]+10, spike2Coords[1]-20)])
        #block handling
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT and xcoord-10>0):
                    xcoord-=4
                elif(event.key == K_RIGHT and xcoord+10<WINDOWWIDTH):
                    xcoord+=4
                elif event.key == K_ESCAPE:
                    pygame.sys.quit()
                    terminate()
        #hit detection
        if spike1Coords[1]-5>=WINDOWHEIGHT-20:
            if (spike1Coords[0]-10 <= xcoord-10 <= spike1Coords[0]+10) or (spike1Coords[0]-10 <= xcoord+10 <= spike1Coords[0]+10):
                terminate()
        if spike2Coords[1]-5>=WINDOWHEIGHT-20:
            if (spike2Coords[0]-10 <= xcoord-10 <= spike2Coords[0]+10) or (spike2Coords[0]-10 <= xcoord+10 <= spike2Coords[0]+10):
                terminate()
        pygame.draw.rect(DISPLAYSURF, GREEN, (xcoord,WINDOWHEIGHT-20, 20,20))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def redraw(things):
    DISPLAYSURF.fill(WHITE)
    for thing in things:
        DISPLAYSURF.blit(thing[0], thing[1])
        
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
def terminate():
    pygame.quit()
    sys.exit()
main()
