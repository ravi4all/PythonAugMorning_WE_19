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

bg_1 = pygame.image.load("bg_1.png")
bg_2 = pygame.image.load("bg_1.png")

bg = pygame.image.load("bg_1.png")

bgImg_height = bg_1.get_height()

def showSpeed(s):
    font = pygame.font.SysFont(None,30)
    text = font.render("Speed : {}".format(s),True,red)
    screen.blit(text,(10,10))

bg1_X = 0
bg1_Y = 0

bg2_X = 0
bg2_Y = -height

moveX = 0
moveY = 0

carX = 220
carY = height - img_height

moveCarY = 0

rotateRight = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_UP]:
        moveCarY += 0.1
        moveY += 0.5
        if carY < 250:
            moveCarY = 0
    elif keypressed[pygame.K_DOWN]:
        moveY -= 0.1
    else:
        moveY = 0

    screen.fill(white)
    screen.blit(bg, (0,0))
    screen.blit(bg_1,(bg1_X,bg1_Y))
    screen.blit(bg_2, (bg2_X, bg2_Y))

    img = pygame.transform.rotate(img,rotateRight)
    screen.blit(img,(carX,carY))

    carY -= moveCarY

    bg1_Y += moveY
    bg2_Y += moveY

    showSpeed(moveY)
    if bg1_Y > height:
        bg1_Y = -height
    elif bg2_Y > height:
        bg2_Y = -height

    pygame.display.update()