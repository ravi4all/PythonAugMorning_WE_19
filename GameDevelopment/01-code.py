import pygame

pygame.init()

screen = pygame.display.set_mode((1000,500))

black = 0,0,0
white = 255,255,255
red = 255,0,0

screen.fill(red)

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()