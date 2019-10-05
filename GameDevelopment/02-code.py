import pygame

pygame.init()

screen = pygame.display.set_mode((1000,500))

black = 0,0,0
white = 255,255,255
red = 255,0,0

screen.fill(black)
var = 100
while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # for i in range(10):
    #     for j in range(10):
    #         x = j * 52
    #         y = i * 52
    #         pygame.draw.rect(screen, white, [x, y, 50, 50])

    for i in range(20):
        for j in range(0,20):
            v = int(i + j + 1) % 2
            if v == 1:
                color = black
            else:
                color = white
            x = j * 100
            y = i * 100
            pygame.draw.rect(screen,color,(x,y,100,100))

    pygame.display.flip()