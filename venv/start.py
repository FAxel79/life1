import random, pygame, math

run = True
pygame.init()
WWidht = 1500
HHeight = 900
win = pygame.display.set_mode((WWidht, HHeight))
pygame.display.set_caption("Life")


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()