from graphics import*


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
    jah1 = True
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
    pass
    #lives screen here

def lives_difficulty():
    pass
    #lives and difficulty selct here



def game_mp():
    pass
    #make your multiplayer game here

def how_to_play():
    pass
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
        elif 350 < x < 600 and 365 < y < 420:
            clear(win)
            how_to_play()
        if 1 < x < 3 and 2 < y < 4:
            #life.undraw()
            #lifehighlight.draw(win)
            pass
        else:
            #lifehighlight.undraw()
            #life.draw(win)
            pass

            
            
