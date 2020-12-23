import pygame
import random, time, sys
from audio import sound_preview

pygame.init()

# [Customs]
SW, SH = 800, 600
HW, HH = (SW / 2), (SH / 2)
FPS = 120

# [Colors]
RED =           (214, 33,  33)
GREEN =         (0,   255, 0)
BLUE =          (0,   0,   255)
LIGHT_RED =     (255, 30,  0)
LIGHT_GREEN =   (33,  255, 33)
LIGHT_BLUE =    (0,   76,  255)
GRAY =          (119, 118, 110)
BLACK =         (0,   0,   0)
WHITE =         (255, 255, 255)

SD = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Car Switch-Surface Game")
CLOCK = pygame.time.Clock()


# [Original Image]
car_image = pygame.image.load("assets/car0.png")
road_background = pygame.image.load("assets/road1.png")
settings_icon = pygame.image.load("assets/settings icon.png")
playBtn = pygame.image.load("assets/play-button.png")
settings_background = pygame.image.load("assets/menu_background.png")

# [Scaled Image]
road1_copy = pygame.transform.scale(road_background, (SW, SH+200))
settings_bgcopy = pygame.transform.scale(settings_background, (SW+50, SH+50))
playBtn_copy = pygame.transform.scale(playBtn, (95, 95))
settings_copy = pygame.transform.scale(settings_icon, (60, 60))

# [variables]
car_width = 63
highscore = 0
pause = True


def text_objects(text, font, color):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()

def render_txt(text, size, x, y, color, font="freesansbold.ttf"):
    fontstyle = pygame.font.Font(font, size)
    textsurf, textrect = text_objects(text, fontstyle, color)
    textrect.center = ((x), (y))
    SD.blit(textsurf, textrect)

def render_img(image, x, y):
    SD.blit(image, (x, y))

def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        render_txt("CAR SWITCH -", 60, 400, 120, RED)
        render_txt(" SURFACE GAME", 60, 395, 220, RED)
        render_txt("Highest Score: " + str(highscore), 25, 395, 445, WHITE)
        pygame.display.update()
        render_img(road1_copy, 0, 0)
        # [car image on the main menu ]
        render_img(car_image, (SW * 0.46), (SH * 0.9))
        button("PLAY", 352, 330, 100, 50, GREEN, LIGHT_GREEN, "play")
        button("SETTINGS", 170, 520, 175, 50, BLUE, LIGHT_BLUE, "options")
        button("QUIT", 530, 520, 100, 50, RED, LIGHT_RED, "quit_prompt")
        # pygame.display.update()
        CLOCK.tick(FPS)

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    selection = ["play", "quit_prompt", "intro", "options", "menu",
                 "pause", "unpause", "audio", "m_on", "m_off", "exit_active", "exit_inactive"]

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(SD, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == selection[0]:
                countdown()
            elif action == selection[1]:
                on_exit()
            elif action == selection[2]:
                instruction()
            elif action == selection[3]:
                settings_menu()
            elif action == selection[4]:
                intro_loop()
            elif action == selection[5]:
                paused()
            elif action == selection[6]:
                unpaused()
            elif action == selection[7]:
                audio()
            elif action == selection[8]:
                music_on()
            elif action == selection[9]:
                music_off()
            elif action == selection[10]:
                yes_on_exit()
            elif action == selection[11]:
                no_on_exit()
    else:
        pygame.draw.rect(SD, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext, WHITE)
    textrect.center = ((x + (w / 2)),(y + (h / 2)))
    SD.blit(textsurf, textrect)

def on_exit():
    not_exit = True
    while not_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        settings_bgcopy = pygame.transform.scale(settings_background, (400, 300))
        SD.blit(settings_bgcopy, (195, 135))
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textSurf1, textRect1 = text_objects("Are you sure you want to exit?", smalltext, BLACK)
        textRect1.center = ((397), (230))
        SD.blit(textSurf1, textRect1)
        button("Yes", 280, 300, 75, 50, RED, LIGHT_RED, "exit_active")
        button("No", 430, 300, 75, 50, GREEN, LIGHT_GREEN, "exit_inactive")
        pygame.display.update()
        CLOCK.tick(FPS)

def yes_on_exit():
    pygame.quit()
    sys.exit()

def no_on_exit():
    intro_loop()


def audio():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        render_img(settings_bgcopy, -20, -20)
        render_txt("MUSIC", 40, 397, 150, BLACK)
        button("ON", 350, 230, 85, 50, GREEN, LIGHT_GREEN, "m_on")
        button("OFF", 350, 300, 85, 50, RED, LIGHT_RED, "m_off")
        pygame.display.update()
        CLOCK.tick(FPS)

def music_on():
    sound_preview(1)
    settings_menu()

def music_off():
    sound_preview(0)
    settings_menu()

def instruction():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SD.blit(settings_bgcopy, (-20,-20))
        largetext = pygame.font.Font("freesansbold.ttf", 80)
        mediumtext = pygame.font.Font("freesansbold.ttf", 40)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("This car game introduces the concept of newtons law of motion in a vehicle", smalltext, BLACK)
        textRect.center = ((398), (200))
        textSurf1, textRect1 = text_objects("Hitting another vehicle mut be avoided.", smalltext, BLACK)
        textRect1.center = ((398), (220))
        TextSurf, TextRect = text_objects("INSTRUCTION", largetext, BLACK)
        TextRect.center = ((400), (100))
        SD.blit(TextSurf, TextRect)
        SD.blit(textSurf, textRect)
        SD.blit(textSurf1, textRect1)
        stextSurfc, stextRect = text_objects("ARROW LEFT : LEFT TURN", smalltext, BLACK)
        stextRect.center = ((400), (400))
        htextSurfc, htextRect = text_objects("ARROW RIGHT : RIGHT TURN", smalltext, BLACK)
        htextRect.center = ((400), (450))
        atextSurfc, atextRect = text_objects("A : ACCELERATION", smalltext, BLACK)
        atextRect.center = ((400), (500))
        rtextSurfc, rtextRect = text_objects("B : BRAKE", smalltext, BLACK)
        rtextRect.center = ((400), (550))
        ptextSurfc, ptextRect = text_objects("P : PAUSE", smalltext, BLACK)
        ptextRect.center = ((400), (350))
        sTextSurfc, sTextRect = text_objects("CONTROLS", mediumtext, BLACK)
        sTextRect.center = ((400), (300))
        SD.blit(sTextSurfc, sTextRect)
        SD.blit(stextSurfc, stextRect)
        SD.blit(htextSurfc, htextRect)
        SD.blit(atextSurfc, atextRect)
        SD.blit(rtextSurfc, rtextRect)
        SD.blit(ptextSurfc, ptextRect)
        button("BACK", 600, 500, 100, 50, BLUE, LIGHT_BLUE, "options")
        pygame.display.update()
        CLOCK.tick(FPS)

def settings_menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SD.blit(settings_bgcopy, (-20, -20))
        mediumtext = pygame.font.Font("freesansbold.ttf", 40)
        textSurf1, textRect1 = text_objects("SETTINGS", mediumtext, BLACK)
        textRect1.center = ((397), (150))
        SD.blit(textSurf1, textRect1)
        button("HOW TO PLAY", 310, 230, 175, 50, GREEN, LIGHT_GREEN, "intro")
        button("MUSIC", 344, 300, 100, 50, GREEN, LIGHT_GREEN, "audio")
        button("BACK", 344, 370, 100, 50, GREEN, LIGHT_GREEN, "menu")
        pygame.display.update()
        CLOCK.tick(FPS)

def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SD.blit(road1_copy, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("PAUSED", largetext, BLACK)
        TextRect.center = ((HW), (HH))
        SD.blit(TextSurf, TextRect)
        button("CONTINUE", 120, 450, 150, 50, GREEN, LIGHT_GREEN, "unpause")
        button("RESTART", 320, 450, 150, 50, BLUE, LIGHT_BLUE, "play")
        button("MAIN MENU", 520, 450, 170, 50, RED, LIGHT_RED, "menu")
        pygame.display.update()
        CLOCK.tick(FPS)

def unpaused():
    global pause
    pause = False

def countdown_bg():
    font = pygame.font.Font("freesansbold.ttf", 25)
    x = (SW * 0.46)
    y = (SH * 0.79)
    render_img(road1_copy, 0, 0)
    text = font.render("Dodged: 0", True, BLACK)
    scoretext = font.render("   Score: 0", True, RED)
    SD.blit(text, (5, 550))
    SD.blit(scoretext, (5, 520))
    render_img(car_image, x, y)
    button("||", 708, 31, 50, 50, BLUE, LIGHT_BLUE, "pause")

def countdown():
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        SD.fill(GRAY)
        countdown_bg()
        render_txt("3", 115, HW, HH, BLACK)
        pygame.display.update()
        CLOCK.tick(1)
        SD.fill(GRAY)
        countdown_bg()
        render_txt("2", 115, HW, HH, BLACK)
        pygame.display.update()
        CLOCK.tick(1)
        SD.fill(GRAY)
        countdown_bg()
        render_txt("1", 115, HW, HH, BLACK)
        pygame.display.update()
        CLOCK.tick(1)
        SD.fill(GRAY)
        countdown_bg()
        render_txt("GO!", 115, HW, HH, BLACK)
        pygame.display.update()
        CLOCK.tick(1)
        game_loop()


def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load("assets/bus1.png")
    elif obs == 1:
        obs_pic = pygame.image.load("assets/car1.png")
    elif obs == 2:
        obs_pic = pygame.image.load("assets/car2.png")
    elif obs == 3:
        obs_pic = pygame.image.load("assets/car5.png")
    elif obs == 4:
        obs_pic = pygame.image.load("assets/car3.png")
    elif obs == 5:
        obs_pic = pygame.image.load("assets/car4.png")
    elif obs == 6:
        obs_pic = pygame.image.load("assets/car6.png")
    elif obs == 7:
        obs_pic = pygame.image.load("assets/car7.png")

    SD.blit(obs_pic, (obs_startx+10, obs_starty+10))

def score_board(passed, score):
    font = pygame.font.Font("freesansbold.ttf", 25)
    text = font.render("Dodged: " + str(passed), True, BLACK)
    scoretext = font.render("   Score: " + str(score), True, RED)
    SD.blit(text, (5, 550))
    SD.blit(scoretext, (5, 520))

def crash_fail():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SD.blit(road1_copy, (0, 0))
        render_txt("Car Crashed!!!", 70, HW, HH-100, BLACK)
        button("SETTINGS", 120, 400, 150, 50, GREEN, LIGHT_GREEN, "options")
        button("PLAY AGAIN", 320, 400, 150, 50, BLUE, LIGHT_BLUE, "play")
        button("MAIN MENU", 520, 400, 170, 50, RED, LIGHT_RED, "menu")
        pygame.display.update()

def game_loop():
    global x_change, y_change, pause

    x = (SW * 0.46)
    y = (SH * 0.79)
    x_change = 0
    y_change = 0
    obs = 0
    obstacle_speed = 15
    obs_startx = random.randrange(200, (SW - 200))
    obs_starty = -750
    obs_width = 65
    obs_height = 105
    passed = 0
    level = 0
    score = 0
    y2 = 7
    fps = 120

    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                if event.key == pygame.K_RIGHT:
                    x_change = 15
                if event.key == pygame.K_w:
                    obstacle_speed += 2
                if event.key == pygame.K_s:
                    obstacle_speed -= 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                # ===== SPEED UP & BREAK =====
                # if event.key == pygame.K_UP:
                #     y_change = -5
                # if event.key == pygame.K_DOWN:
                #     y_change = 5

        x += x_change
        y += y_change
        SD.fill(GRAY)

        rel_y = y2 % road1_copy.get_rect().width
        SD.blit(road1_copy, (0, rel_y - road1_copy.get_rect().width))
        SD.blit(road1_copy, (1000, rel_y - road1_copy.get_rect().width))

        if rel_y < 800:
            SD.blit(road1_copy, (0, rel_y))
            SD.blit(road1_copy, (1000, rel_y))

        y2 += obstacle_speed-5
        obs_starty -= (obstacle_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        render_img(car_image, x, y)
        score_board(passed, score)

        if x > 670 - car_width or x < 130:
            crash_fail()

        if x > SW - (car_width + 130) or x < 130:
            crash_fail()

        if obs_starty > SH:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170, (SW - 170))
            obs = random.randrange(0, 7)
            passed += 1
            score = passed * 10
            highscore = score
            if int(passed) % 10 == 0:
                level += 1
                obstacle_speed += 5
                render_txt("STAGE "+str(level), 70, HW, HH, BLACK)
                pygame.display.update()
                time.sleep(3)
                sound_preview(1)

        if y < obs_starty + obs_height:
            if x > obs_startx+3 and x < obs_startx+3 + obs_width-3 or x + car_width-3 > obs_startx+3 and x + car_width-3 < obs_startx+3 + obs_width-3:
                crash_fail()

        button("||", 708, 31, 50, 50, BLUE, LIGHT_BLUE, "pause")
        pygame.display.update()
        CLOCK.tick(FPS)

if __name__ == '__main__':
    sound_preview(1)
    intro_loop()
    pygame.quit()
    sys.exit()
