import pygame
import random
from time import sleep

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 512
background_width = 1024
aladdin_width = 90
aladdin_height = 55
genie_width = 110
genie_height = 67

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))
    
def runGame():
    global gamepad, aladdin, clock, background1, background2
    global genie, lamp, magic
    
    isShotGenie = False
    magic_count = 0
    
    lamp_xy = []
    
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

                elif event.key == pygame.K_LCTRL:
                        lamp_x = x + aladdin_width
                        lamp_y = y + aladdin_height/2
                        lamp_xy.append([lamp_x, lamp_y])
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    
        gamepad.fill(WHITE)

        background1_x -= 2
        background2_x -= 2

        if background1_x == -background_width:
            background1_x = background_width

        if background2_x == -background_width:
            background2_x = background_width

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)

        y += y_change
        if y < 0:
            y = 0
        elif y > pad_height - aladdin_height:
            y = pad_height - aladdin_height
            
        genie_x -= 7
        if genie_x <= 0:
            genie_x = pad_width
            genie_y = random.randrange(0, pad_height)
            
        if len(lamp_xy) != 0:
            for i, lxy in enumerate(lamp_xy):
                lxy[0] += 15
                lamp_xy[i][0] = lxy[0]

                if lxy[0] > genie_x:
                    if lxy[1] > genie_y and lxy[1] < genie_y + genie_height:
                        lamp_xy.remove(lxy)
                        isShotGenie = True

                if lxy[0] >= pad_width:
                    try:
                        lamp_xy.remove(lxy)
                    except:
                        pass

        drawObject(aladdin, x, y)
        
        if len(lamp_xy) != 0:
            for lx, ly in lamp_xy:
                drawObject(lamp, lx, ly)

        if not isShotGenie:
            drawObject(genie, genie_x, genie_y)
        else:
            drawObject(magic, genie_x, genie_y)
            magic_count += 1
            if magic_count > 5:
                magic_count = 0
                genie_x = pad_width
                genie_y = random.randrange(0, pad_height - genie_height)
                isShotGenie = False        

        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
    
def initGame():
    global gamepad, aladdin, clock, background1, background2
    global genie, lamp, magic
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('Flying')
    aladdin = pygame.image.load('images/Aladdin4.png')
    background1 = pygame.image.load('images/desert2.jpg')
    background2 = background1.copy()
    genie = pygame.image.load('images/genie3.png')
    magic = pygame.image.load('images/magic1.png')
    lamp = pygame.image.load('images/lamp1.png')
    
    clock = pygame.time.Clock()
    runGame()

initGame()
