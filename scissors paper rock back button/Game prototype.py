from graphics import*
from game import *

width = 1000
height = 700
lives = 0
difficulty = ""

#window
win = GraphWin("Rock Paper Scissors", width, height)
win.setBackground('White')

single_player = False
multiplayer = False

def start():
    square5 = Rectangle(Point(350,310), Point(650, 390))
    square5.setFill('blue')
    square5.setOutline('white')
    square5.setWidth(0)
    square5.draw(win)
    txt2 = Text(Point(width//2,height//2), "Start")
    txt2.draw(win)
    txt2.setTextColor('white')
    txt2.setFace('courier')
    txt2.setSize(60)
    jah1= True
    while jah1:
        #get mouse
        e=win.getMouse()
        #get x
        x=e.getX()
        #get y
        y=e.getY()
        #if click top button
        if 350 < x < 650 and 310 < y < 390:
            txt2.undraw()
            square5.undraw()
            #what happens when you hit start
            if single_player == True:
                lives()
            if multiplayer == True:
                lives_difficulty()
def lives():
    img4 = Image(Point(500,100, "Jah.png"))
    img4.draw(win)


def lives_difficulty():
    pass
    #lives and difficulty selct here
def game_sp():
    clear(win)
    backbtn = Image(Point(36,36), "back.png")
    backbtn.draw(win)
    txt11 = Text(Point(100,100), ("Choose Lives: "))
    txt11.setTextColor('black')
    txt11.setFace('courier')
    txt11.setSize(15)
    txt11.draw(win)
    txt12 = Text(Point(120,300), ("Choose Difficulty: "))
    txt12.setTextColor('black')
    txt12.setFace('courier')
    txt12.setSize(15)
    txt12.draw(win)
    img4 = Image(Point(200,100), "Jah.png")
    img4.draw(win)
    img5 = Image(Point(250,100), "Jah.png")
    img5.draw(win)
    img6 = Image(Point(300,100), "Jah.png")
    img6.draw(win)
    img7 = Image(Point(350,100), "Jah.png")
    img7.draw(win)
    img8 = Image(Point(400,100), "Jah.png")
    img8.draw(win)
    img9 = Image(Point(450,100), "Jah.png")
    img9.draw(win)
    img10 = Image(Point(500,100), "Jah.png")
    img10.draw(win)
    img19 = Image(Point(500,100), "Jah.png")
    img19.draw(win)
    img11 = Image(Point(200,100), "Jah2.png")
    img12 = Image(Point(250,100), "Jah2.png")
    img13 = Image(Point(300,100), "Jah2.png")
    img14 = Image(Point(350,100), "Jah2.png")
    img15 = Image(Point(400,100), "Jah2.png")
    img16 = Image(Point(450,100), "Jah2.png")
    img17 = Image(Point(500,100), "Jah2.png")
    img18 = Image(Point(500,100), "Jah2.png")
    txt13 = Text(Point(270,300), ("-Easy "))
    txt13.setTextColor('black')
    txt13.setFace('courier')
    txt13.setSize(15)
    txt13.draw(win)
    txt14 = Text(Point(280,325), ("-Medium "))
    txt14.setTextColor('black')
    txt14.setFace('courier')
    txt14.setSize(15)
    txt14.draw(win)
    txt15 = Text(Point(270,350), ("-Hard "))
    txt15.setTextColor('black')
    txt15.setFace('courier')
    txt15.setSize(15)
    txt15.draw(win)
    lives = 7
    diff = ''
    while True:
        mouse = win.getMouse()
        x = mouse.getX()
        y = mouse.getY()
        print(x,y)
        hearts = [img4,img5,img6,img7,img8,img9,img10,img19]
        hearts2 = [img11,img12,img13,img14,img15,img16,img17,img18]
        if 4 < x < 68 and 4 < y < 68:
            clear(win)
            for heart in hearts:
                heart.undraw()
            for heart in hearts2:
                heart.undraw()
            backbtn.undraw()
            txt11.undraw()
            txt12.undraw()
            txt13.undraw()
            txt14.undraw()
            txt15.undraw()
            mode_select()
        if 180 < x < 220 and 85 < y < 120:
            for heart in hearts:
                heart.undraw()
            for herat in hearts2:
                herat.undraw()
            for i in range(0,1):
                try:
                    hearts2[i].draw(win)
                except:
                    pass
            for i in range(1,7):
                hearts[i].draw(win)
            lives = 1
        if 230 < x < 270 and 85 < y < 120:
            for heart in hearts:
                heart.undraw()
            for herat in hearts2:
                herat.undraw()
            for i in range(0,2):
                try:
                    hearts2[i].draw(win)
                except:
                    pass
            for i in range(2,7):
                hearts[i].draw(win)
            lives = 2
        if 280 < x < 320 and 85 < y < 120:
            for heart in hearts:
                heart.undraw()
            for herat in hearts2:
                herat.undraw()
            for i in range(0,3):
                try:
                    hearts2[i].draw(win)
                except:
                    pass
            for i in range(3,7):
                hearts[i].draw(win)
            lives = 3
        if 330 < x < 370 and 85 < y < 120:
            for heart in hearts:
                heart.undraw()
            for herat in hearts2:
                herat.undraw()
            for i in range(0,4):
                try:
                    hearts2[i].draw(win)
                except:
                    pass
            for i in range(4,7):
                hearts[i].draw(win)
            lives = 4
        if 380 < x < 420 and 85 < y < 120:
            for heart in hearts:
                heart.undraw()
            for herat in hearts2:
                herat.undraw()
            for i in range(0,5):
                try:
                    hearts2[i].draw(win)
                except:
                    pass
            for i in range(5,7):
                hearts[i].draw(win)
            lives = 5
        if 420 < x < 470 and 85 < y < 120:
            for heart in hearts:
                heart.undraw()
            for herat in hearts2:
                herat.undraw()
            for i in range(0,6):
                try:
                    hearts2[i].draw(win)
                except:
                    pass
            for i in range(6,7):
                hearts[i].draw(win)
            lives = 6
        if 470 < x < 520 and 85 < y < 120:
            for heart in hearts:
                heart.undraw()
            for herat in hearts:
                herat.undraw()
            for i in range(0,7):
                try:
                    hearts2[i].draw(win)
                except:
                    pass
            lives = 7
        if 243 < x < 291 and 295 < y < 310:
            diff = 'easy'
            break
        if 243 < x < 310 and 320 < y < 330:
            diff = 'medium'
            break
        if 243 < x < 291 and 340 < y < 360:
            diff = 'hard'
            break
    game(diff,lives)




def game_mp():
    clear(win)
    backbtn2 = Image(Point(36,36), "back.png")
    backbtn2.draw(win)
    txt8 = Text(Point(510,320), ("Take turns picking between rock paper and scissors "))
    txt8.draw(win)
    txt8.setTextColor('black')
    txt8.setFace('courier')
    txt8.setSize(15)
    txt9 = Text(Point(510,340), ("multiplayer follows the same rules as normal rock paper scissors"))
    txt9.draw(win)
    txt9.setTextColor('black')
    txt9.setFace('courier')
    txt9.setSize(15)
    txt10 = Text(Point(510,360), ("the person with the most points at the end wins!"))
    txt10.draw(win)
    txt10.setTextColor('black')
    txt10.setFace('courier')
    txt10.setSize(15)
    #make your multiplayer game here
    while True:
        mouse = win.getMouse()
        x = mouse.getX()
        y = mouse.getY()
        print(x,y)
        if 4 < x < 68 and 4 < y < 68:
            clear(win)
            backbtn2.undraw()
            txt8.undraw()
            txt9.undraw()
            txt10.undraw()
            mode_select()

def how_to_play():
    clear(win)
    backbtn3 = Image(Point(36,36), "back.png")
    backbtn3.draw(win)
    txt5 = Text(Point(450,280), ("You Play a game of rock, paper, scissors but with a bot"))
    txt5.draw(win)
    txt5.setTextColor('black')
    txt5.setFace('courier')
    txt5.setSize(20)
    txt6 = Text(Point(450,300), ("You can change the amount of lives and difficulty"))
    txt6.draw(win)
    txt6.setTextColor('black')
    txt6.setFace('courier')
    txt6.setSize(20)
    txt7 = Text(Point(450,320), ("Rules: Have Fun :)"))
    txt7.draw(win)
    txt7.setTextColor('black')
    txt7.setFace('courier')
    txt7.setSize(20)
    while True:
        mouse = win.getMouse()
        x = mouse.getX()
        y = mouse.getY()
        print(x,y)
        if 4 < x < 68 and 4 < y < 68:
            clear(win)
            backbtn3.undraw()
            txt5.undraw()
            txt6.undraw()
            txt7.undraw()
            mode_select()

    #make how to play instruction screen here
def clear(win):
    for item in win.items:
        item.undraw()
        win.update()
#lives

def mode_select():
  #title
    square1 = Rectangle(Point(20,20), Point(980, 200))
    square1.setFill('blue')
    square1.setOutline('white')
    square1.setWidth(0)
    square1.draw(win)

    #top rectangle
    square2 = Rectangle(Point(350,300), Point(600, 250))
    square2.setFill('blue')
    square2.setOutline('white')
    square2.setWidth(0)
    square2.draw(win)

    #middle
    square3 = Rectangle(Point(350,305), Point(600, 360))
    square3.setFill('blue')
    square3.setOutline('white')
    square3.setWidth(0)
    square3.draw(win)

    #bottom
    square4 = Rectangle(Point(350,365), Point(600, 420))
    square4.setFill('blue')
    square4.setOutline('white')
    square4.setWidth(0)
    square4.draw(win)
    #title text
    txt = Text(Point(500,110), "Rock Paper Scissors")
    txt.draw(win)
    txt.setTextColor('white')
    txt.setFace('courier')
    txt.setSize(60)
    #Text on Top Button
    txt = Text(Point(470,280), "Single Player")
    txt.draw(win)
    txt.setTextColor('white')
    txt.setFace('courier')
    txt.setSize(20)
    #Text on Middle Button
    txt = Text(Point(470,340), "MultiPlayer")
    txt.draw(win)
    txt.setTextColor('White')
    txt.setFace('courier')
    txt.setSize(20)
    #Text on Bottom Button
    txt = Text(Point(470,400), "How To Play")
    txt.draw(win)
    txt.setTextColor('White')
    txt.setFace('courier')
    txt.setSize(20)
    #Information PNG
    img = Image(Point(780,500), "Scissors.png")
    img.draw(win)
    img2 = Image(Point(290,555), "Paper (2).png")
    img2.draw(win)
    img3 = Image(Point(230,280), "rock.png")
    img3.draw(win)
    #game loop
    jah = True

    #game loop
    jah = True
    while jah:
        #get mouse
        e=win.getMouse()    
        #get x
        x=e.getX()
        #get y
        y=e.getY()
        #if click top button
        if 350 < x < 600 and 250 < y < 300:
            txt.undraw()
            square2.undraw()
            square4.undraw()
            square3.undraw()
            img2.undraw()
            img.undraw()
            img3.undraw()
            clear(win)
            single_player = True
            game_sp()
            lives_difficulty()
            
        #if click middle button
        elif 350 < x < 600 and 305 < y < 360:
            clear(win)
            img2.undraw()
            img.undraw()
            img3.undraw()
            square2.undraw()
            square4.undraw()
            square3.undraw()
            multiplayer = True
            game_mp()
        #if click bottom button
        if 350 < x < 600 and 365 < y < 420:
            txt.undraw()
            square2.undraw()
            square4.undraw()
            square3.undraw()
            img2.undraw()
            img.undraw()
            img3.undraw()
            clear(win)
            clear(win)
            how_to_play()            
#how to play tab
   


mode_select()  
