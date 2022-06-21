import pygame 
import random
import time


#Initialising
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snakes and Ladders")

#Screen Components
gameBoard = pygame.image.load("Snakes and Ladders img.png")
gameBoard = pygame. transform. scale(gameBoard, (600, 560))
bg = pygame.image.load("dice bg.jpg")
bg = pygame. transform. scale(bg, (850, 800))
arrow = pygame.image.load("arrow.png")
arrow = pygame. transform. scale(arrow, (50, 50))

bx = 200
by = 0

#Player Pieces
p1 = pygame.image.load("Player1.jpg")
p1 = pygame. transform. scale(p1, (30, 30))

p2 = pygame.image.load("Player 2.jpg")
p2 = pygame. transform. scale(p2, (30, 30))

gx = 30
gy = 100

px = 30
py = 300

#Diceroll button 
button = pygame.Rect(30,530,70,70)

font1 = pygame.font.SysFont("comicsansms", 25)
font2 = pygame.font.SysFont("comicsansms", 18)

def board():
    screen.blit(bg, (0,0))
    screen.blit(gameBoard, (bx,by))
    screen.blit(arrow, (30,520))

def player1(x,y):
    screen.blit(p1, (x,y))

def player2(x,y):
    screen.blit(p2, (x,y))

#Dice roll function
def randomNumber():
    diceroll = random.randint(1, 6)
    if diceroll == 1:
        dice = pygame.image.load("dice1.png")
    elif diceroll == 2:
        dice = pygame.image.load("dice2.png")
    elif diceroll == 3:
        dice = pygame.image.load("dice3.png")
    elif diceroll == 4:
        dice = pygame.image.load("dice4.png")
    elif diceroll == 5:
        dice = pygame.image.load("dice5.jpg")
    elif diceroll == 6:
        dice = pygame.image.load("dice6.png")

    dice = pygame. transform. scale(dice, (70, 70))

    return (dice, diceroll)

def players():
    txt1 = font1.render("Player 1",True,(255,0,0))
    screen.blit(txt1,[100,100])
    txt2 = font1.render("Player 2",True,(255,0,0))
    screen.blit(txt2,[100,300])

def rollFirst():
    txt3 = font2.render("It is your Turn",True,(255,0,0))
    screen.blit(txt3,[30,170])

def rollSecond():
    txt4 = font2.render("It is now your Turn",True,(255,0,0))
    screen.blit(txt4,[30,370])

#Game Running Loop
running = True

turn = 'Player 1'

while running:
    screen.fill((0,255,195))
    board()
    players()

    if turn == 'Player 1':
        rollFirst()
    else:
        rollSecond()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                randomNumber()
                dice, diceroll = randomNumber()
                screen.blit(dice,(20,440))
                print(diceroll)

            #Player 1 Movement

            if randomNumber() and turn == 'Player 1':
                turn = 'Player 2'
                if diceroll == 6 and gx == 30 and gy == 100:
                    gx = 315
                    gy = 500
                    turn = 'Player 1'

                elif gx in range(315,475) and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll != 6:
                    gx += (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx in range(315,475) and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll == 6:
                    gx += (40*diceroll)
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
            #5
                elif gx == 475 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll != 6:
                    gx += (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                    
                elif gx == 475 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll == 6:
                    gx += (5*diceroll)
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
            #6
                elif gx == 515 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll <= 4:
                    gx += (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                    
                elif gx == 515 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll > 4 and diceroll != 6:
                    gx += (40*4)
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 515 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll == 6:
                    gx = gx + (40*4) - (40*(diceroll-5))
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
            #7
                elif gx == 555 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll <= 3:
                    gx += (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 555 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll > 3 and diceroll != 6:
                    gx = gx +(40*3)-(40*(diceroll-4))
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 555 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll == 6:
                    gx = gx + (40*3) - (40*(diceroll-4))
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
            #8
                elif gx == 595 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll <= 2:
                    gx += (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 595 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll > 2 and diceroll != 6:
                    gx = gx +(40*2)-(40*(diceroll-3))
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 595 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll == 6:
                    gx = gx + (40*2) - (40*(diceroll-3))
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
            #9
                elif gx == 635 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll == 1:
                    gx += 40
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 635 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll > 1 and diceroll != 6:
                    gx = gx +(40)-(40*(diceroll-2))
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 635 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll == 6:
                    gx = gx + (40) - (40*(diceroll-2))
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
            #10
                elif gx >= 675 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll != 6:
                    gx -=(40*(diceroll-1))
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx >= 675 and (gy == 500 or gy == 400 or gy == 300 or gy == 200 or gy == 100) and diceroll == 6:
                    gx -=(40*(diceroll-1))
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450

                #Row 2

                elif gx > 475 and gx <= 675 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and diceroll != 6:
                    gx -= (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                    
                elif gx > 475 and gx <= 675 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and diceroll == 6:
                    gx -= (40*5)
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                
                elif gx>515 and gx<=675 and diceroll != 6 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50):
                    gx -= (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx>515 and gx<=675 and diceroll == 6 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50):
                    gx -= (40*diceroll)
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                
                elif gx==515 and diceroll != 6 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50):
                    gx -= (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx==515 and diceroll == 6 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50):
                    gx -= (40*5)
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450

                elif gx == 475 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and diceroll<5:
                    gx -= (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 475 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and  diceroll == 5:
                    gx = gx-(40*4)
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 475 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and  diceroll == 6:
                    gx = gx-(40*3)
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450

                elif gx == 435 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and diceroll<4:
                    gx -= (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 435 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and  diceroll >= 4 and diceroll != 6:
                    gx = gx-(40*3)+(40*(diceroll-4))
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 435 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and  diceroll == 6:
                    gx -= 40
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                
                elif gx == 395 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and diceroll < 3:
                    gx -= (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 395 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and diceroll >= 3 and diceroll !=6:
                    gx = gx-(40*2)+(40*(diceroll-3))
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 395 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and  diceroll == 6:
                    gx += 40
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450

                elif gx == 355 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and diceroll==1:
                    gx -= (40*diceroll)
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 355 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and  diceroll >= 2 and diceroll !=6:
                    gx = gx-(40*1)+(40*(diceroll-2))
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 355 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and  diceroll == 6:
                    gx += (40*3)
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450

                elif gx == 315 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and diceroll!=6:
                    gx += (40*(diceroll-1))
                    gy -= 50
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450
                        
                elif gx == 315 and (gy == 450 or gy == 350 or gy == 250 or gy == 150 or gy == 50) and diceroll==6:
                    gx += (40*(diceroll-1))
                    gy -= 50
                    turn = 'Player 1'
                    if gx == 635 and gy == 450:
                        gx = 675
                        gy = 300
                    elif gx == 435 and gy == 350:
                        gx = 395
                        gy = 500
                    elif gx == 555 and gy == 450:
                        gx = 515
                        gy = 250
                    elif gx ==555 and gy == 250:
                        gx = 595
                        gy = 100
                    elif gx == 515 and gy == 150:
                        gx = 635
                        gy = 350
                    elif gx == 555 and gy == 50:
                        gx = 675
                        gy = 150
                    elif gx == 475 and gy == 50:
                        gx = 355
                        gy = 300
                    elif gx == 435 and gy == 500:
                        gx = 475
                        gy = 250
                    elif gx == 355 and gy == 400:
                        gx = 395
                        gy = 250
                    elif gx ==595 and gy == 400:
                        gx = 675
                        gy = 500
                    elif gx == 315 and gy == 300:
                        gx = 355
                        gy = 150
                    elif gx == 555 and gy == 300:
                        gx = 475
                        gy = 450

            #Player 2 Movements    
                    
            elif randomNumber() and turn == 'Player 2':
                turn = 'Player 1'
                if diceroll == 6 and px == 30 and py == 300:
                    px = 315
                    py = 500
                    turn = 'Player 2'

                elif px in range(315,475) and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll != 6:
                    px += (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px in range(315,475) and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll == 6:
                    px += (40*diceroll)
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
            #5
                elif px == 475 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll != 6:
                    px += (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                    
                elif px == 475 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll == 6:
                    px += (5*diceroll)
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
            #6
                elif px == 515 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll <= 4:
                    px += (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                    
                elif px == 515 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll > 4 and diceroll != 6:
                    px += (40*4)
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 515 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll == 6:
                    px = px + (40*4) - (40*(diceroll-5))
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
            #7
                elif px == 555 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll <= 3:
                    px += (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 555 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll > 3 and diceroll != 6:
                    px = px +(40*3)-(40*(diceroll-4))
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 555 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll == 6:
                    px = px + (40*3) - (40*(diceroll-4))
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
            #8
                elif px == 595 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll <= 2:
                    px += (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 595 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll > 2 and diceroll != 6:
                    px = px +(40*2)-(40*(diceroll-3))
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 595 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll == 6:
                    px = px + (40*2) - (40*(diceroll-3))
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
            #9
                elif px == 635 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll == 1:
                    px += 40
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 635 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll > 1 and diceroll != 6:
                    px = px +(40)-(40*(diceroll-2))
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 635 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll == 6:
                    px = px + (40) - (40*(diceroll-2))
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
            #10
                elif px >= 675 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll != 6:
                    px -=(40*(diceroll-1))
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px >= 675 and (py == 500 or py == 400 or py == 300 or py == 200 or py == 100) and diceroll == 6:
                    px -=(40*(diceroll-1))
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450

                #Row 2

                elif px > 475 and px <= 675 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and diceroll != 6:
                    px -= (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                    
                elif px > 475 and px <= 675 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and diceroll == 6:
                    px -= (40*5)
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                
                elif px>515 and px<=675 and diceroll != 6 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50):
                    px -= (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px>515 and px<=675 and diceroll == 6 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50):
                    px -= (40*diceroll)
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                
                elif px==515 and diceroll != 6 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50):
                    px -= (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px==515 and diceroll == 6 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50):
                    px -= (40*5)
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450

                elif px == 475 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and diceroll<5:
                    px -= (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 475 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and  diceroll == 5:
                    px = px-(40*4)
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 475 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and  diceroll == 6:
                    px = px-(40*3)
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450

                elif px == 435 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and diceroll<4:
                    px -= (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 435 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and  diceroll >= 4 and diceroll != 6:
                    px = px-(40*3)+(40*(diceroll-4))
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 435 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and  diceroll == 6:
                    px -= 40
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                
                elif px == 395 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and diceroll < 3:
                    px -= (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 395 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and diceroll >= 3 and diceroll !=6:
                    px = px-(40*2)+(40*(diceroll-3))
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 395 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and  diceroll == 6:
                    px += 40
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450

                elif px == 355 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and diceroll==1:
                    px -= (40*diceroll)
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 355 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and  diceroll >= 2 and diceroll !=6:
                    px = px-(40*1)+(40*(diceroll-2))
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 355 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and  diceroll == 6:
                    px += (40*3)
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450

                elif px == 315 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and diceroll!=6:
                    px += (40*(diceroll-1))
                    py -= 50
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450
                        
                elif px == 315 and (py == 450 or py == 350 or py == 250 or py == 150 or py == 50) and diceroll==6:
                    px += (40*(diceroll-1))
                    py -= 50
                    turn = 'Player 2'
                    if px == 635 and py == 450:
                        px = 675
                        py = 300
                    elif px == 435 and py == 350:
                        px = 395
                        py = 500
                    elif px == 555 and py == 450:
                        px = 515
                        py = 250
                    elif px ==555 and py == 250:
                        px = 595
                        py = 100
                    elif px == 515 and py == 150:
                        px = 635
                        py = 350
                    elif px == 555 and py == 50:
                        px = 675
                        py = 150
                    elif px == 475 and py == 50:
                        px = 355
                        py = 300
                    elif px == 435 and py == 500:
                        px = 475
                        py = 250
                    elif px == 355 and py == 400:
                        px = 395
                        py = 250
                    elif px ==595 and py == 400:
                        px = 675
                        py = 500
                    elif px == 315 and py == 300:
                        px = 355
                        py = 150
                    elif px == 555 and py == 300:
                        px = 475
                        py = 450

            

                
    player1(gx,gy)
    player2(px,py)
    pygame.display.update()
    time.sleep(1.3)
pygame.quit()
quit()
