import pygame
import random

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 512
background_width = 1024

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))
    
def runGame():
    global gamepad, aircraft, clock, background1, background2
    global genie
    
    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background1_x = 0
    background2_x = background_width

    genie_x = pad_width
    genie_y = random.randrange(0, pad_height)

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    
        y += y_change
        gamepad.fill(WHITE)

        background1_x -= 2
        background2_x -= 2

        genie_x -= 7
        if genie_x <= 0:
            genie_x = pad_width
            genie_y = random.randrange(0, pad_height)
            
        if background1_x == -background_width:
            background1_x = background_width

        if background2_x == -background_width:
            background2_x = background_width

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)
        drawObject(genie, genie_x, genie_y)
        drawObject(aircraft, x, y)
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
    
def initGame():
    global gamepad, aircraft, clock, background1, background2
    global genie
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('Flying')
    aircraft = pygame.image.load('images/Aladdin4.png')
    background1 = pygame.image.load('images/desert2.jpg')
    background2 = background1.copy()
    genie = pygame.image.load('images/genie3.png')
    
    clock = pygame.time.Clock()
    runGame()

initGame()
