import pygame

pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

def showSpeed(s):
    font = pygame.font.SysFont(None,30)
    text = font.render("Speed : {}".format(s),True,red)
    screen.blit(text,(10,10))

x = 50
y = 50
moveX = 0
moveY = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         moveX = 1
        #     elif event.key == pygame.K_LEFT:
        #         moveX = -1
        # elif event.type == pygame.KEYUP:
        #     moveX = 0

    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_RIGHT]:
        moveX += 0.01
    elif keypressed[pygame.K_LEFT]:
        moveX -= 0.01
    else:
        moveX = 0

    screen.fill(white)

    pygame.draw.rect(screen,red,(x,y,50,50))
    x += moveX
    # print(x,moveX)

    showSpeed(moveX)

    if x > width:
        x = -50
    elif x < -50:
        x = width

    pygame.display.update()