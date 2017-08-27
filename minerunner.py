import sys, pygame, time
pygame.init()

# Note: If this program does not detect keyboard input,
# it is likely because you are on OS X and not using a
# framework build of Python :(

# Map legend
# 0 - Air
# 1 - Dirt

# The map is indexed by [y, x]
block_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 1],
]
position = [0, 0]  
size = width, height = 320, 240
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("assets/banana.png")
ballrect = ball.get_rect()


def main():
    global ballrect
    map = build_map()
    while 1:
        speed = [0, 0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_LEFT:
                    speed[0] = -1
                elif event.key == pygame.K_RIGHT:
                    speed[0] = 1
                elif event.key == pygame.K_DOWN:
                    speed[1] = -1
                elif event.key == pygame.K_UP:
                    speed[1] = 1

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


def build_map():
    map2 = []
    for row in block_map:
        for i in range(0, 32):
            row2 = []
            for block in row:
                for i in range(0, 32):
                    row2.append(block)
            map2.append(row2)
    return map2


if __name__ == "__main__":
    main()