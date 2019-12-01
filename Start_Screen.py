import pygame
import time
import math
import random
from pygame import mixer
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
crimson = (220, 20, 60)
sea_green = (46, 139, 87)
maroon = (128, 0, 0)
pale_green = (124, 205, 124)
block_color = (53, 115, 255)

Spaceship_width = 128
# Set screen
gameDisplay = pygame.display.set_mode((display_width, display_height))
# Set caption
pygame.display.set_caption('Protect Your Farm')
# Set icon
icon = pygame.image.load('chicken.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
# Set background
background = pygame.image.load('26664.jpg')

SpaceShipImg = pygame.image.load('startup.png')

ChickenImg = []
num_of_chickens = 10
for i in range(num_of_chickens):
    ChickenImg.append(pygame.image.load('chicken.png'))

BulletImg = pygame.image.load('bullet.png')
Bullet_state = "ready"

pause = False

# Fun ctions
def show_score(count):
    font = pygame.font.SysFont("Courier", 30, True)
    text = font.render( "SCORE: " + str(count), True, (255, 246, 143))
    gameDisplay.blit(text, (0, 0))

def Chicken(x, y, i):
    gameDisplay.blit(ChickenImg[i], (x, y))

def SpaceShip(x, y):
    gameDisplay.blit(SpaceShipImg, (x, y))

def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    gameDisplay.blit(BulletImg, (x + 48, y + 40))
def checkCollision(ChickenX, ChikenY, BulletX, BulletY):
    distance = math.sqrt(math.pow(ChickenX-BulletX, 2)+math.pow(ChikenY-BulletY, 2))
    if distance < 27:
        return True
    else:
        return False
def text_objects(text, font):
    textSurface = font.render(text, True, (236, 171, 83))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('Courier', 115, "bold")
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()

def win():
    #texttt = pygame.font.SysFont('Bauhaus 93', 30, True)
    # = texttt.render("YOUR SCORE IS:" + str(show_score()), True, () )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(pygame.image.load('youwin.jpg'), (0, 0))
        button("Try Again", 270, 50, 120, 50, maroon, crimson, gameloop)
        button("Quit", 410, 50, 120, 50, sea_green, pale_green, quitgame)

        pygame.display.update()
        clock.tick(15)


def gameOver():
    txtt = pygame.font.SysFont("Algerian", 30, True)
    #textt = txtt.render("Press key R to Restart or key Q to Quit", True, (0, 255, 0))

    txt = pygame.font.SysFont("Algerian", 95, True)
    text = txt.render("GAME OVER", True, (0, 255, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(pygame.image.load('gameover.jpg'), (0, 0))
        #gameDisplay.blit(textt, (30, 380))
        gameDisplay.blit(text, (100, 200))
        button("Try Again", 150, 450, 120, 50, maroon, crimson, gameloop)
        button("Quit", 550, 450, 120, 50, sea_green, pale_green, quitgame)
                #quitgame()
            #elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_r :
                    #gameloop()
                #if event.key == pygame.K_q:
                    #quitgame()
        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(pygame.image.load('start_screen1.jpg'), (0, 0))
        start_screenIMG = pygame.image.load('start_screen.png')
        gameDisplay.blit(start_screenIMG, (0, 50))
        largeText = pygame.font.SysFont('Courier', 70, True)
        display_text = largeText.render("START", True, maroon)
        gameDisplay.blit(display_text, (260, 330))
        button("Play", 450, 100, 120, 50, maroon, crimson, gameloop)
        button("Quit", 600, 100, 120, 50, sea_green, pale_green, quitgame)

        pygame.display.update()
        clock.tick(15)

def continues():
    global pause
    pause = False

def paused():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        gameDisplay.blit(pygame.image.load('start_screen1.jpg'), (0, 0))
        start_screenIMG = pygame.image.load('start_screen.png')
        gameDisplay.blit(start_screenIMG, (0, 50))
        largeText = pygame.font.SysFont('Courier', 70, True)
        display_text = largeText.render("PAUSED", True, maroon)
        gameDisplay.blit(display_text, (240, 330))

        button("Continue", 450, 100, 120, 50, maroon, crimson, continues)
        button("Quit", 600, 100, 120, 50, sea_green, pale_green, quitgame)

        pygame.display.update()
        clock.tick(15)

# x, y: coodinate, w: width, h: height, ic: icon color, ac: when hover color
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
             action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("Courier", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

# Main game loop
def gameloop():
    # Variables
    global Bullet_state
    global pause
    score_value = 0

    # Add music
    mixer.music.load('Friday-night-synthwave-electronic-music.mp3')
    mixer.music.play()
    mixer.music.rewind()

    # SpaceShip
    SpaceShipX = display_width * 0.45
    SpaceShipY = display_height * 0.8
    x_change = 0

    # Array Chicken
    ChickenX = []
    ChickenY = []
    ChickenX_change = []
    ChickenY_change = []
    for i in range(num_of_chickens):
        ChickenX.append(random.randrange(0, display_width))
        ChickenY.append(random. randrange(50, 200))
        ChickenX_change.append(0.5)
        ChickenY_change.append(30)

    # Bullet
    BulletX = 0
    BulletY = 500
    BulletX_change = 0
    BulletY_change = 20

    # Main loop
    gameExit = False
    while not gameExit:
        gameDisplay.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                if event.key == pygame.K_SPACE:
                    if Bullet_state is "ready":
                        Bullet_Sound = mixer.Sound('Shooting.wav')
                        Bullet_Sound.play()
                        # get the current x coordinate of the spaceship
                        BulletX = SpaceShipX
                        fire_bullet(BulletX, BulletY)
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        # Chicken movement
        for i in range(num_of_chickens):
            # Game over
            if SpaceShipY < ChickenY[i] + 32:
                #if SpaceShipX > ChickenX[i] and SpaceShipX < ChickenX[i] + 32 or SpaceShipX + Spaceship_width > ChickenX[i] and SpaceShipX + Spaceship_width < ChickenX[i] + 32:
                    #BulletY = 1000
                    #BulletX = 1000
                if ChickenY[i] > 200:
                    for j in range(num_of_chickens):
                        ChickenX[j] = 2000
                gameOver()
                break

            ChickenX[i] += ChickenX_change[i]
            Chicken(ChickenX[i], ChickenY[i], i)
            if ChickenX[i] <= 0:
                ChickenX_change[i] = 2
                ChickenY[i] += ChickenY_change[i]
            if ChickenX[i] >= 780:
                ChickenX_change[i] = -2
                ChickenY[i] += ChickenY_change[i]

            # Check collision
            collision = checkCollision(ChickenX[i], ChickenY[i], BulletX, BulletY)
            if collision:
                fire_Sound = mixer.Sound('bum.wav')
                fire_Sound.play()
                BulletY = display_height * 0.8
                Bullet_state = "ready"
                score_value += 5
                ChickenX[i] = random.randrange(0, display_width)
                ChickenY[i] = random.randrange(50, 400)
        SpaceShipX += x_change
        # Check boundaries
        if SpaceShipX <= 0:
            SpaceShipX = 0
        elif SpaceShipX >= display_width - 80:
            SpaceShipX = display_width - 80

        # Bullet movement
        if BulletY <= 0:
            BulletY = 480
            Bullet_state = "ready"

        if Bullet_state is "fire":
            fire_bullet(BulletX, BulletY)
            BulletY -= BulletY_change
        if score_value >= 50:
            win()

        show_score(score_value)
        SpaceShip(SpaceShipX, SpaceShipY)

        pygame.display.update()
        clock.tick(60)
# Main Function
game_intro()
gameloop()
pygame.display.update()
pygame.quit()
quit()