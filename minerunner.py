import sys, pygame
pygame.init()

# Map legend
# 0 - Air
# 1 - Dirt

# The map is indexed by [y, x]
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 1],
]  
position = [0, 0]  
size = width, height = 320, 240
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("assets/ball.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            speed[0] = 1

    # Movement
    ballrect = ballrect.move(speed)
    position[0] = position[0] + speed[0]
    position[1] = position[1] + speed[1]

    # Check for falling (air below position)
    if map[position[1] + 1][position[0]] == 0:
        print('falling!')
    
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = 0
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = 0

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()


# TODO items:
# - make game speed independent of mainloop
# - make keyboard work on mac
# - transform the map so it is [x, y]
