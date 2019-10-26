import random,time
def game(diff,lives):
     #make this what the player chose
    difficulty = diff #make this the difficulty (easy, medium ,hard ,super hard)

    timeoptions = {'easy': 180,'medium':120,'hard':60,'super hard': 'gay'}

    winchoices = [('rock','scissors'),('scissors','paper'),('paper','rock')]
    choices = ['rock','paper','scissors']
    timez = timeoptions.get(difficulty)
    live = lives
    score = 0
    bot = 0
    now = time.time()
    while True:
        playerchoice = input('Pick something! ')
        computerchoice = random.choice(choices)
        if playerchoice.lower() in choices and time.time() - now > timez:
            if live > 1:
                if playerchoice == computerchoice:
                    print('Tie') #this is if they tie, im not sure what you want to do here so do it yourself >;)
                elif (playerchoice,computerchoice) in winchoices:
                    score+=1
                    print('You won!! the current score is: '+str(score)+' and for the bot!: '+str(bot)) #this is if they win just make a text where it changes the value based on score ill put print for demonstration
                else:
                    live -= 1
                    bot+=1
                    print('You lost! Current lives: '+str(live)+' the current score is: '+str(score)+' and for the bot!: '+str(bot)) # this is when they loose do the same thing as win, ill use print for demonstration
            else:
                name = input('You ran out of lives please input your name: ')
                user_choice = input("Do you want to play again? ")
                if user_choice.lower() in ['y','yes']:
                    live = lives
                    score = 0
                    bot = 0
                    pass
                else:
                    break
        elif playerchoice.lower() not in choices:
            print('Invalid response please try again! ')
        else:
            name = input('You ran out of time please input your name: ')
            print('Wins: '+str(score)+' Difficulty: '+str(hard))
        













game('easy',1)


















#github.com/jean1398reborn/Augmented
