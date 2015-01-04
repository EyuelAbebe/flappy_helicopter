#!/usr/local/bin/python2.7
import pygame
import time
import random 


pygame.init()

size = width, height = 800, 600
imgheight = 40
imgwidth = 80
black = (0,0,0)
white = (255,255,255)

surface = pygame.display.set_mode(size)
pygame.display.set_caption("Helicopter'")

clock = pygame.time.Clock()

def helicopter(x, y, image):
    surface.blit(img, (x,y))

def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type is pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type is pygame.KEYDOWN:
            continue

        return event.key
    return None

def msgSurface(msg):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 120)

    titleTextSurf, titleTextRect = makeTextObjs(msg, largeText)
    titleTextRect.center = width/2, height/2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue: ', smallText)
    typTextRect.center = width/2, (height/2 + 100)
    surface.blit(typTextSurf, typTextRect)
   
    pygame.display.update()
    time.sleep(1)
    
    while replay_or_quit() == None:
        clock.tick()

    main()
        
def gameOver():
    msgSurface("Kaboooom!!")

img = pygame.image.load('helicopter.png')

def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, white, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, white, [x_block, y_block + block_height + gap, block_width, block_height])

def main():
    x, y = 150, 200
    x_move, y_move = 0, 2

    x_block = width
    y_block = 0
    block_width = 75
    block_height = random.randint(0, height)
    gap = imgheight * 3
    block_move = 3


    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -3
                if event.key == pygame.K_DOWN:
                    y_move = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_move = 3
                if event.key == pygame.K_LEFT:
                    x_move = -3
            if event.type == pygame.K_UP:
                if event.key.K_RIGHT:
                    x_move = 0

        y += y_move
        x += x_move

        surface.fill(black)
        helicopter(x,y, img)
        
        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move

        if y > height - 40 or y < 0:
            gameOver()
        if x_block < (-1 * block_width):
            x_block = width
            block_height = random.randint(0, height)

        pygame.display.update()    
        clock.tick(60)
main()
pygame.quit()
quit()
