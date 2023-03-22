import pygame
import random
import math
import PySimpleGUI as sg
import database_interface
import contact_information_window

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Catch all the cookies!")
icon = pygame.image.load("monster.png")
pygame.display.set_icon(icon)
background = pygame.image.load("underground.png")

score_arrey = []

monsterImg = pygame.image.load("monster.png")
monsterX = 300
monsterY = 200
monsterX_change = 0
monsterY_change = 0

cookieImg = pygame.image.load("cookie.png")
cookieX = random.randint(0, 668)
cookieY = random.randint(0, 468)

running = True

score = 0
font = pygame.font.SysFont("comicsansms", 32)
end_font = pygame.font.SysFont("comicsansms", 64)

start_time = pygame.time.get_ticks() # uzzinam laiku kopš palaižam spēli
max_time = 30 # sek


def show_monster(x, y):
    screen.blit(monsterImg, (x, y))

def show_cookie(x, y):
    screen.blit(cookieImg, (x,y))
def is_cookie_eaten(mX, mY, cX, cY):
    distance = math.sqrt(math.pow((mX+64/2) - (cX+32/2), 2) + (math.pow((mY+32) - (cY+16), 2)))
    if distance <= 48:
        return True
    return False

def show_score(score):
    score_text = font.render("Score:" + str(score), True, (255,255,255))
    screen.blit(score_text, (10, 10))

def show_time(time):
    time_text = font.render("Time remaining:" + str(time_remaining), True, (255,255,255))
    screen.blit(time_text, (400, 10)) 

def show_game_over(score):
    screen.blit(background, (0,0))
    end_text = end_font.render("Game over", True, (255,0,0))
    screen.blit(end_text, (200, 150)) 
    score_text = font.render("Your score is:" + str(score), True, (255,0,0))
    screen.blit(score_text, (230, 250))
    x=1

    if x==2:
        pass
    else: 
        x=2   
        layout = [[sg.Text('Enter your name:'), sg.InputText()],
            [sg.Button('Submit'), sg.Button('Scores')]]

        window = sg.Window('High Scores', layout)

        event, values = window.Read()
        if event == 'Submit':
            x=2
            
        if event == 'Score':
            database_interface.insert_contact(values['-NAME-'], score)
            sg.popup("Information submitted!")
        elif event == 'Show Table':
            contact_information_window.create()

            

while running:
    screen.fill((0, 0, 0)) # RGB - red green blue
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                monsterX_change = -0.25
                monsterY_change = 0
            if event.key == pygame.K_RIGHT:
                monsterX_change = 0.25
                monsterY_change = 0
            if event.key == pygame.K_UP:
                monsterX_change = 0
                monsterY_change = -0.25
            if event.key == pygame.K_DOWN:
                monsterX_change = 0
                monsterY_change = 0.25
    time = pygame.time.get_ticks() # uzzinam cik tgd ir laiks
    time_elapsed = (time - start_time)/1000
    time_remaining = int(max_time - time_elapsed)


    if monsterX >= 636:
        monsterX = 636
    elif monsterX <= 0:
        monsterX = 0
    elif monsterY >= 440:
        monsterY = 440
    elif monsterY <= 0:
        monsterY = 0

    if is_cookie_eaten(monsterX, monsterY, cookieX, cookieY):
        cookieX =  random.randint(0, 668)
        cookieY = random.randint(0, 468)
        score += 1 
        
    monsterX += monsterX_change
    monsterY += monsterY_change
    show_monster(monsterX, monsterY)
    show_cookie(cookieX, cookieY)
    show_score(score)
    show_time(time)
    if (time_remaining<0):
        show_game_over(score)

    pygame.display.update()