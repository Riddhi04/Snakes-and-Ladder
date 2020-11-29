import pygame
import time
import random

pygame.init()

display_width= 1000
display_height= 750


black= (0,0,0)
white= (255,255,255)
red= (200,0,0)
blue= (0,50,100)
green= (0,200,0)

blue_bright= (0,0,200)
red_bright= (255,0,0)
c1= (0,200,100)


X= (90)
Y= (112.5)

rx= 75

k= 1
rcount= 0
bcount= 0
gcount= 0
ycount= 0

rx= 75
ry= 690
bx= 55
by= 690
gx= 35
gy= 690
yx= 15
yy= 690

tok= 0

condition= 0

sum1= 0

count1= 0

dice_roll= 0

MIN_PLAYER_COUNT= 1

playerCount= MIN_PLAYER_COUNT

font= pygame.font.Font('freesansbold.ttf', 100)

font1= pygame.font.Font('freesansbold.ttf', 30)


gameDisplay=pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Snakes and Ladders')

clock=pygame.time.Clock()

imgsl1 = pygame.image.load('sl5.png')
snakesandladders= pygame.image.load('snakes and ladders.png')
redtoken = pygame.image.load('red.png')
bluetoken = pygame.image.load('blue.png')
greentoken = pygame.image.load('green.png')
yellowtoken = pygame.image.load('yellow.png')

def pic(img, x, y):
    gameDisplay.blit(img,(x, y))

def text_objects(text, font, color):
    textSurface= font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, size, e, f):
     largeText = pygame.font.SysFont('courier new', size, bold=True)
     TextSurf , TextRect = text_objects(text, largeText, white)
     TextRect.center = (e, f)
     gameDisplay.blit(TextSurf, TextRect)


def textSandL (text,size,len,hei):
    message_display(text,size,len,hei)
    
    
def show_dice(roll, clr):
    dice_number= font.render(str(roll), True, clr)
    gameDisplay.blit(dice_number, (800, 510))

def dice_roll():
    global sum1
    global count1
    global playerCount
    global condition
    global rcount
    global bcount
    global gcount
    global ycount
    global tok

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    roll = random.randint(1, 6)
    caption = font1.render("You lose a turn!", True, (0, 255, 0))
    caption1 = font1.render("You lose a turn!", True, (0, 0, 0))
    print("roll=", roll)

    if count1 == 0:
        sum1 = 0
    if roll == 6 and count1 == 2:
        print("insidde roll == 6 and count1 == 2:")
        show_dice(roll, (255, 0, 0))
        gameDisplay.blit(caption, (750, 600))
        pygame.display.update()
        pygame.time.delay(600)
        show_dice(roll, (0, 0, 0))
        gameDisplay.blit(caption1, (750, 600))
        clock.tick(15)

        sum1 = 0
        count1 = 0
        playerCount = playerCount + 1
        if(playerCount > tok):
            playerCount = MIN_PLAYER_COUNT
        return 18
    if roll == 6 and count1 < 2:
        print(" inside roll == 6 and count1 < 2")
        clock.tick(15)
        pygame.display.update()
        sum1 = sum1 + roll
        count1 = count1 + 1

    if roll != 6 and count1 == 0:
        print("inside  roll != 6 and count1 == 0")
        sum1 = roll
        playerCount = playerCount + 1
        if (playerCount > tok):
            playerCount = MIN_PLAYER_COUNT
        if (rcount==1 or bcount==1 or gcount==1 or ycount==1):
            condition=1
            print("condition = ",condition)
        

    if roll != 6 and count1 > 0:
        print("insde roll != 6 and count1 > 0")
        sum1 = sum1 + roll
        count1 = 0
        playerCount = playerCount + 1
        if (playerCount > tok):
            playerCount = MIN_PLAYER_COUNT
        condition=1
        print("condition = ",condition)

    show_dice(roll, (255, 0, 0))
    pygame.display.update()
    pygame.time.delay(500)
    clock.tick(500)
    show_dice(roll, (0, 0, 0))
    print("sum1 = ",sum1)
    
    return sum1

    
def board(number):
    a= (display_width * 0.075)
    b= (display_height * 0.9)

    global tok
    
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start()
                crashed = True
            print(event)
                            
        gameDisplay.fill(black)
        textSandL("SNAKES & LADDERS", 80, display_width/2, display_height*0.075)
        pic(snakesandladders,X,Y)

        if tok==2 :
            gameDisplay.blit(bluetoken,(bx,by))
            gameDisplay.blit(redtoken,(rx,ry))

        elif tok==3 :
            gameDisplay.blit(greentoken,(gx,gy))
            gameDisplay.blit(bluetoken,(bx,by))
            gameDisplay.blit(redtoken,(rx,ry))

        else:
            gameDisplay.blit(yellowtoken,(yx,yy))
            gameDisplay.blit(greentoken,(gx,gy))
            gameDisplay.blit(bluetoken,(bx,by))
            gameDisplay.blit(redtoken,(rx,ry))

        end=button("ROLL",780,300,80,50,c1,green,number,'cont')
        button("EXIT",780,400,80,50,red,red_bright,number,"quit")
        if end==-1:
            textSandL("YOU WIN!!", 45 , 850,197)
            pygame.display.update()
            clock.tick(15)
            crashed=True
            return -1

        pygame.display.update()


        clock.tick(15)

def players():
    global tok
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            button("2 PLAYERS",300,550,125,50,blue,blue_bright,0,None)
            button("3 PLAYERS",450,550,125,50,blue,blue_bright,0,None)
            button("4 PLAYERS",600,550,125,50,blue,blue_bright,0,None)
            mouse= pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 300+125 > mouse[0] > 300 and 550 + 50 > mouse[1] > 550:
                if click[0]==1:
                    tok = 2
                    end=board(2)
                    if end==-1:
                        pygame.time.delay(10000)
                        crashed=True
            if 450+125 > mouse[0] > 450 and 550 + 50 > mouse[1] > 550:
                if click[0]==1:
                    tok = 3
                    end=board(3)
                    if end==-1:
                        pygame.time.delay(10000)
                        crashed = True
            if 600+125 > mouse[0] > 600 and 550 + 50 > mouse[1] > 550:
                if click[0]==1:
                    tok = 4
                    end=board(4)
                    if end==-1:
                        pygame.time.delay(10000)
                        crashed=True
        pygame.display.update()
        clock.tick(15)


def SL(x1, y1):
    print("inside SL")
    print(" x1 = ",x1)
    if (583 < x1 < 639) and (675 < y1 < 728):
        print("ladder 1")
        return 61, -183
    
    if (460 < x1 < 515) and (614 < y1 < 671):
        print("ladder 2")
        return -122 , -183 

    if (280 < x1 < 334) and (553 < y1 < 607):
        print("ladder 3")
        return 0 , -244

    if (523 < x1 < 577) and (430 < y1 < 486):
        print("ladder 4")
        return -122 , -122

    if (217 < x1 < 273) and (307 < y1 < 363):
        print("ladder 5")
        return -122 , -122

    if (584 < x1 < 645) and (489 < y1 < 550):
        return -183, 183

    if (156 < x1 < 217) and (119 < y1 < 180):
        return 0, 427

    if (460 < x1 < 521) and (242 < y1 < 303):
        return -305, 244   

    if (400 < x1 < 461) and (181 < y1 < 242):
        return 244, 183
    if x1< 90 or y1< 118:
        return -1, -1
    else:
        return 0,0
   

def button(msg, x, y, w, h, ic, ac, number, action=None): #ic=inactive color ac=active color
    
    mouse= pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    global tok
    global k
    global rcount
    global bcount
    global gcount
    global ycount
    global rx
    global bx
    global gx
    global yx
    global ry
    global by
    global gy
    global yy
    global playerCount
    global condition
    
    mouse= pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] >y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action== 'play':
                players()
            elif action== 'cont':
                print('Current Player', playerCount)
                w=dice_roll()
                print("w= ", w)
                print('Current Player Score', sum1, "  playrCount =", playerCount)
                print("CONDITION = ", condition)
                if tok== 2:
                    if condition== 1:
                        print("inside condition==1")
                        if playerCount== 1:
                            print(" inside playerCount==1")
                            playerCount= 2
                        else:
                            playerCount= playerCount-1
                    if w== 18:
                        return
                    if (playerCount== 1):
                        print("1st player", "   rcount = ", rcount)
                        if condition== 1:
                            playerCount= 2
                        if rcount== 0:
                            if w> 6 and w!= 12 :
                                if w == 17:
                                    k1 = rx + (61 * (w - 6 - 1))
                                    rx = 665
                                    ry = ry - 61
                                else:
                                    if w== 15:
                                        rx = rx + 40 + (61*(w - 6 - 1))
                                        rx= rx + 61
                                        ry= ry - 183
                                    else:
                                        rx = rx + 40 + (61*(w - 6 - 1))
                                rcount=1
                        else:
                            if w!= 6 and w!= 12 and w!= 18:
                                k1 = rx + (61 * w)
                                k2 = rx - (61 * w)
                                if 700 > rx > 105 and ((727 > ry > 677) or
                                                       (607 > ry > 553) or
                                                       (487 > ry > 430) or
                                                       (362 > ry > 307) or
                                                       (241 > ry > 183)):
                                    if k1> 700:
                                        rx = 665
                                        ry = ry - 61
                                        rx = rx - (k1 - rx) + 61
                                    else:
                                        rx = rx + (61 * w)
                                    print("old rx =",rx)
                                    dx, dy = SL(rx, ry)
                                    if dx==-1 and dy==-1:
                                        rx=117
                                        ry=144
                                        return -1
                                    else:
                                        rx = rx + dx
                                        ry = ry + dy
                                    print("new rx = ", rx)
                                else:
                                    if k2 < 95:
                                        rx = 115
                                        ry = ry - 61
                                        rx = rx + (rx - k2) - 61
                                    else:
                                        rx = rx - (61 * w)
                                    print("old rx =", rx)
                                    dx, dy = SL(rx, ry)
                                    if dx==-1 and dy==-1:
                                        rx=117
                                        ry=144
                                        return -1
                                    else:
                                        rx = rx + dx
                                        ry = ry + dy
                                    print("new rx =", rx)
                    else:
                        print("2nd player")
                        if condition== 1:
                            playerCount= 1
                        if bcount== 0:
                            if w> 6 and w!= 12 :
                                if w == 17:
                                    k1 = bx + (61 * (w - 6 - 1))
                                    bx = 665
                                    by = by - 61
                                else:
                                    if w== 15:
                                        bx = bx + 60 + (61*(w - 6 - 1))
                                        bx= bx + 61
                                        by= by - 183
                                    else:
                                        bx = bx + 60 + (61*(w - 6 - 1))
                                bcount= 1
                        else:
                            if w!= 6 and w!= 12 and w!= 18:
                                k1 = bx + (61 * w)
                                k2 = bx - (61 * w)
                                if 700 > bx > 105 and ((727 > by > 677) or
                                                       (607 > by > 553) or
                                                       (487 > by > 430) or
                                                       (362 > by > 307) or
                                                       (241 > by > 183)):
                                    if k1> 700:
                                        bx = 665
                                        by = by - 61
                                        bx= bx - (k1 - bx) + 61 
                                    else:
                                        bx = bx + (61 * w)
                                    print("old bx =", bx)
                                    dx, dy= SL(bx, by)
                                    if dx==-1 and dy==-1:
                                        bx=117
                                        by=144
                                        return -1
                                    else:
                                        bx = bx + dx
                                        by = by + dy
                                    print("new bx =", bx)
                                else:
                                    if k2 < 95:
                                        bx = 115
                                        by = by - 61
                                        bx = bx + (bx - k2) - 61
                                    else:
                                        bx = bx - (61 * w)
                                    print("old bx =", bx)
                                    dx, dy = SL(bx, by)
                                    if dx==-1 and dy==-1:
                                        bx=117
                                        by=144
                                        return -1
                                    else:
                                        bx = bx + dx
                                        by = by + dy
                                    print("new bx =", bx)
                    
                elif tok == 3:
                    if condition== 1:
                        print("inside condition==1")
                        if playerCount== 1:
                            print(" inside playerCount==1")
                            playerCount= 3
                        else:
                            playerCount= playerCount-1
                    if w== 18:
                        return
                    if (playerCount== 1):
                        print("1st player", "   rcount = ", rcount)
                        if condition== 1:
                            playerCount= 2
                        if rcount== 0:
                            if w> 6 and w!= 12 :
                                if w == 17:
                                    k1 = rx + (61 * (w - 6 - 1))
                                    rx = 665
                                    ry = ry - 61
                                else:
                                    if w== 15:
                                        rx = rx + 40 + (61*(w-6-1))
                                        rx= rx + 61
                                        ry= ry - 183
                                    else:
                                        rx = rx + 40 + (61*(w-6-1))
                                rcount= 1
                        else:
                            if w!= 6 and w!= 12 and w!= 18:
                                k1 = rx + (61 * w)
                                k2 = rx - (61 * w)
                                if 700 > rx > 105 and ((727 > ry > 677) or
                                                       (607 > ry > 553) or
                                                       (487 > ry > 430) or
                                                       (362 > ry > 307) or
                                                       (241 > ry > 183)):
                                    if k1> 700:
                                        rx = 665
                                        ry = ry - 61
                                        rx = rx - (k1 - rx) + 61
                                    else:
                                        rx = rx + (61 * w)
                                    print("old rx =", rx)
                                    dx, dy = SL(rx, ry)
                                    if dx==-1 and dy==-1:
                                        rx=117
                                        ry=144
                                        return -1
                                    else:                                        
                                        rx = rx + dx
                                        ry = ry + dy
                                    print("new rx = ", rx)
                                else:
                                    if k2 < 95:
                                        rx = 115
                                        ry = ry - 61
                                        rx = rx + (rx - k2) - 61
                                    else:
                                        rx = rx - (61 * w)
                                    print("old rx =", rx)
                                    dx, dy = SL(rx, ry)
                                    if dx==-1 and dy==-1:
                                        rx=117
                                        ry=144
                                        return -1
                                    else:                                        
                                        rx = rx + dx
                                        ry = ry + dy
                                    print("new rx =", rx)
                    elif (playerCount==2):
                        print("2nd player")
                        if condition== 1:
                            playerCount= 3
                        if bcount== 0:
                            if w> 6 and w!= 12 :
                                if w == 17:
                                    k1 = bx + (61 * (w-6-1))
                                    bx = 665
                                    by = by - 61
                                else:
                                    if w== 15:
                                        bx = bx + 60 + (61*(w-6-1))
                                        bx= bx + 61
                                        by= by - 183
                                    else:
                                        bx = bx + 60 + (61*(w-6-1))
                                bcount= 1
                        else:
                            if w!= 6 and w!= 12 and w!= 18:
                                k1 = bx + (61 * w)
                                k2 = bx - (61 * w)
                                if 700 > bx > 105 and ((727 > by > 677) or
                                                       (607 > by > 553) or
                                                       (487 > by > 430) or
                                                       (362 > by > 307) or
                                                       (241 > by > 183)):
                                    if k1>700:
                                        bx = 665
                                        by = by - 61
                                        bx = bx - (k1 - bx) + 61 
                                    else:
                                        bx = bx + (61 * w)
                                    print("old bx =", bx)
                                    dx, dy = SL(bx, by)
                                    if dx==-1 and dy==-1:
                                        bx=117
                                        by=144
                                        return -1
                                    else:                                        
                                        bx = bx + dx
                                        by = by + dy
                                    print("new bx =", bx)
                                else:
                                    if k2 < 95:
                                        bx = 115
                                        by = by - 61
                                        bx = bx + (bx - k2) - 61
                                    else:
                                        bx = bx - (61 * w)
                                    print("old bx =", bx)
                                    dx, dy = SL(bx, by)
                                    if dx==-1 and dy==-1:
                                        bx=117
                                        by=144
                                        return -1
                                    else:                                        
                                        bx = bx + dx
                                        by = by + dy
                                    print("new bx =", bx)
                    else:
                        print("3rd player")
                        if condition== 1:
                            playerCount= 1
                        if gcount== 0:
                            if w> 6 and w!= 12:
                                if w == 17:
                                    k1 = gx + (61 * (w-6-1))
                                    gx = 665
                                    gy = gy - 61
                                else:
                                    if w== 15:
                                        gx = gx + 80 + (61*(w-6-1))
                                        gx= gx + 61
                                        gy= gy - 183
                                    else:
                                        gx = gx + 80 + (61*(w-6-1))
                                gcount= 1
                        else:
                            if w!= 6 and w!= 12 and w!= 18:
                                k1 = gx + (61 * w)
                                k2 = gx - (61 * w)
                                if 700 > gx > 105 and ((727 > gy > 677) or
                                                       (607 > gy > 553) or
                                                       (487 > gy > 430) or
                                                       (362 > gy > 307) or
                                                       (241 > gy > 183)):
                                    if k1> 700:
                                        gx = 665
                                        gy = gy - 61
                                        gx = gx - (k1 - gx) + 61
                                    else:
                                        gx = gx + (61 * w)
                                    print("old gx =", gx)
                                    dx, dy = SL(gx, gy)
                                    if dx==-1 and dy==-1:
                                        gx=117
                                        gy=144
                                        return -1
                                    else:                                        
                                        gx = gx + dx
                                        gy = gy + dy
                                    print("new gx =", gx)
                                else:
                                    if k2 < 95:
                                        gx = 115
                                        gy = gy - 61
                                        gx = gx + (gx - k2) - 61
                                    else:
                                        gx = gx - (61 * w)
                                    print("old gx =", gx)
                                    dx, dy = SL(gx, gy)
                                    if dx==-1 and dy==-1:
                                        gx=117
                                        gy=144
                                        return -1
                                    else:                                        
                                        gx = gx + dx
                                        gy = gy + dy
                                    print("new gx =", gx)
                else: #tok==4:
                    if condition== 1:
                        print("inside condition==1")
                        if playerCount== 1:
                            print(" inside playerCount==1")
                            playerCount= 4
                        else:
                            playerCount= playerCount-1
                    if w== 18:
                        return
                    if (playerCount== 1):
                        print("1st player", "   rcount = ", rcount)
                        if condition== 1:
                            playerCount= 2
                        if rcount== 0:
                            if w> 6 and w!= 12 :
                                if w == 17:
                                    k1 = rx + (61 * (w-6-1))
                                    rx = 665
                                    ry = ry - 61
                                else:
                                    if w== 15:
                                        rx = rx + 40 + (61*(w-6-1))
                                        rx= rx + 61
                                        ry= ry - 183
                                    else:
                                        rx = rx + 40 + (61*(w-6-1))
                                rcount= 1
                        else:
                            if w!= 6 and w!= 12 and w!= 18:
                                k1 = rx + (61 * w)
                                k2 = rx - (61 * w)
                                if 700 > rx > 105 and ((727 > ry > 677) or
                                                       (607 > ry > 553) or
                                                       (487 > ry > 430) or
                                                       (362 > ry > 307) or
                                                       (241 > ry > 183)):
                                    if k1> 700:
                                        rx = 665
                                        ry = ry - 61
                                        rx = rx - (k1 - rx) + 61
                                    else:
                                        rx = rx + (61 * w)
                                    print("old rx =", rx)
                                    dx, dy = SL(rx, ry)
                                    if dx==-1 and dy==-1:
                                        rx=117
                                        ry=144
                                        return -1
                                    else:                                        
                                        rx = rx + dx
                                        ry = ry + dy
                                    print("new rx = ", rx)
                                else:
                                    if k2 < 95:
                                        rx = 115
                                        ry = ry - 61
                                        rx = rx + (rx - k2) - 61
                                    else:
                                        rx = rx - (61 * w)
                                    print("old rx =", rx)
                                    dx, dy = SL(rx, ry)
                                    if dx==-1 and dy==-1:
                                        rx=117
                                        ry=144
                                        return -1
                                    else:                                        
                                        rx = rx + dx
                                        ry = ry + dy
                                    print("new rx =", rx)
                    elif (playerCount== 2):
                        print("2nd player")
                        if condition== 1:
                            playerCount= 3
                        if bcount== 0:
                            if w> 6 and w != 12 :
                                if w == 17:
                                    k1 = bx + (61 * (w-6-1))
                                    bx = 665
                                    by = by - 61
                                else:
                                    if w== 15:
                                        bx = bx + 60 + (61*(w-6-1))
                                        bx = bx+61
                                        by = by-183
                                    else:
                                        bx = bx + 60 + (61*(w-6-1))
                                bcount= 1
                        else:
                            if w!= 6 and w!= 12 and w!= 18:
                                k1 = bx + (61 * w)
                                k2 = bx - (61 * w)
                                if 700 > bx > 105 and ((727 > by > 677) or
                                                       (607 > by > 553) or
                                                       (487 > by > 430) or
                                                       (362 > by > 307) or
                                                       (241 > by > 183)):
                                    if k1> 700:
                                        bx = 665
                                        by = by - 61
                                        bx = bx - (k1 - bx) + 61 
                                    else:
                                        bx = bx + (61 * w)
                                    print("old bx =", bx)
                                    dx, dy = SL(bx, by)
                                    if dx==-1 and dy==-1:
                                        bx=117
                                        by=144
                                        return -1
                                    else:                                        
                                        bx = bx + dx
                                        by = by + dy
                                    print("new bx =", bx)
                                else:
                                    if k2 < 95:
                                        bx = 115
                                        by = by - 61
                                        bx = bx + (bx - k2) - 61
                                    else:
                                        bx = bx - (61 * w)
                                    print("old bx =", bx)
                                    dx, dy = SL(bx, by)
                                    if dx==-1 and dy==-1:
                                        bx=117
                                        by=144
                                        return -1
                                    else:                                        
                                        bx = bx + dx
                                        by = by + dy
                                    print("new bx =", bx)
                    elif playerCount==3:
                        print("3rd player")
                        if condition==1:
                            playerCount=4
                        if gcount==0:
                            if w>6 and w!=12:
                                if w == 17:
                                    k1 = gx + (61 * (w-6-1))
                                    gx = 665
                                    gy = gy - 61
                                else:
                                    if w==15:
                                        gx = gx + 80 + (61*(w-6-1))
                                        gx=gx+61
                                        gy=gy-183
                                    else:
                                        gx = gx + 80 + (61*(w-6-1))
                                gcount=1
                        else:
                            if w!=6 and w!=12 and w!=18:
                                k1 = gx + (61 * w)
                                k2 = gx - (61 * w)
                                if 700 > gx > 105 and ((727 > gy > 677) or
                                                       (607 > gy > 553) or
                                                       (487 > gy > 430) or
                                                       (362 > gy > 307) or
                                                       (241 > gy > 183)):
                                    if k1>700:
                                        gx = 665
                                        gy = gy - 61
                                        gx = gx - (k1 - gx) + 61
                                    else:
                                        gx = gx + (61 * w)
                                    print("old gx =",gx)
                                    dx,dy = SL(gx,gy)
                                    if dx==-1 and dy==-1:
                                        gx=117
                                        gy=144
                                        return -1
                                    else:                                        
                                        gx = gx + dx
                                        gy = gy + dy
                                    print("new gx =",gx)
                                else:
                                    if k2 < 95:
                                        gx = 115
                                        gy = gy - 61
                                        gx = gx + (gx - k2) - 61
                                    else:
                                        gx = gx - (61 * w)
                                    print("old gx =",gx)
                                    dx,dy = SL(gx,gy)
                                    if dx==-1 and dy==-1:
                                        gx=117
                                        gy=144
                                        return -1
                                    else:                                        
                                        gx = gx + dx
                                        gy = gy + dy
                                    print("new gx =",gx)
                    else:
                        print("4th player")
                        if condition==1:
                            playerCount=1
                        if ycount==0:
                            if w>6 and w!=12:
                                if w == 17:
                                    k1 = yx + (61 * (w-6-1))
                                    yx = 665
                                    yy = yy - 61
                                else:
                                    if w==15:
                                        yx = yx + 100 + (61*(w-6-1))
                                        yx=yx+61
                                        yy=yy-183
                                    else:
                                        yx = yx + 100 + (61*(w-6-1))
                                ycount=1
                        else:
                            if w!=6 and w!=12 and w!=18:
                                k1 = yx + (61 * w)
                                k2 = yx - (61 * w)
                                if 700 > yx > 105 and ((727 > yy > 677) or
                                                       (607 > yy > 553) or
                                                       (487 > yy > 430) or
                                                       (362 > yy > 307) or
                                                       (241 > yy > 183)):
                                    if k1>700:
                                        yx = 665
                                        yy = yy - 61
                                        yx = yx - (k1 - yx) + 61
                                    else:
                                        yx = yx + (61 * w)
                                    print("old yx =",yx)
                                    dx,dy = SL(yx,yy)
                                    if dx==-1 and dy==-1:
                                        yx=117
                                        yy=144
                                        return -1
                                    else:                                        
                                        yx = yx + dx
                                        yy = yy + dy
                                    print("new yx =",yx)
                                else:
                                    if k2 < 95:
                                        yx = 115
                                        yy = yy - 61
                                        yx = yx + (yx - k2) - 61
                                    else:
                                        yx = yx - (61 * w)
                                    print("old yx =",yx)
                                    dx,dy = SL(yx,yy)
                                    if dx==-1 and dy==-1:
                                        yx=117
                                        yy=144
                                        return -1
                                    else:                                        
                                        yx = yx + dx
                                        yy = yy + dy
                                    print("new yx =",yx)
                    
                condition=0
                return    
            else:
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        
    rolltext = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, rolltext, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf,textRect)
    

def start():
    quitt = False

    while not quitt:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitt = True
            print(event)
                
        gameDisplay.fill(black)
        pic(imgsl1,display_width*0.2,0.01)
        
        button("PLAY",450,550,80,50,blue,blue_bright,0, "play")

        pygame.display.update()
        clock.tick(15)

start()


pygame.quit()
quit()

