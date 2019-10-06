import pygame

pygame.init()

width = 1200
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0

img = pygame.image.load('car_1.png')
img_width = img.get_width()
img_height = img.get_height()

bg = pygame.image.load("bg_1.png")

def showSpeed(s):
    font = pygame.font.SysFont(None,30)
    text = font.render("Speed : {}".format(s),True,red)
    screen.blit(text,(10,10))

x = 220
y = height - img_height
moveX = 0
moveY = 0
rotateRight = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_UP]:
        moveY -= 0.1
    elif keypressed[pygame.K_DOWN]:
        moveY += 0.1
    # elif keypressed[pygame.K_RIGHT]:
    #     rotateRight -= 0.01
    else:
        moveY = 0

    screen.fill(white)
    screen.blit(bg,(0,0))

    img = pygame.transform.rotate(img,rotateRight)
    screen.blit(img,(x,y))
    y += moveY

    showSpeed(moveY)

    if y > height:
        y = -img_height
    elif y < -img_height:
        y = height

    pygame.display.update()