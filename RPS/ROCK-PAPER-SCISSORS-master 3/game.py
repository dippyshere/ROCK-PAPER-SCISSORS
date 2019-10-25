import random
def game(diff,lives):
     #make this what the player chose
    difficulty = diff #make this the difficulty (easy, medium ,hard ,super hard)

    timeoptions = {'easy': 3,'medium':2,'hard':1,'super hard': 1}

    winchoices = [('rock','scissors'),('scissors','paper'),('paper','rock')]
    choices = ['rock','paper','scissors']
    score = 0

    time = timeoptions.get(difficulty)
    while True:
        playerchoice = input('Pick something! ')
        computerchoice = random.choice(choices)
        if lives > 1:
            if playerchoice == computerchoice:
                print('Tie') #this is if they tie, im not sure what you want to do here so do it yourself >;)
            elif (playerchoice,computerchoice) in winchoices:
                score+=1
                print('You won!! the current score is: '+str(score)) #this is if they win just make a text where it changes the value based on score ill put print for demonstration
            else:
                lives -= 1
                print('You lost! Current lives: '+str(lives)) # this is when they loose do the same thing as win, ill use print for demonstration
        else:
            user_choice = input("Do you want to play again? ")
            if user_choice.lower() in ['y','yes']:
                pass
            else:
                break


