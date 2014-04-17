############# Guess the Number game ###################
############# -- Prerna Satija ########################


# initialize global variables used in your code


import simplegui
import random
import math

high = 100
low = 0
count= math.ceil(math.log(high - low + 1)/math.log(2))
n=count
secretNum = 0



# helper function to start and restart the game
def new_game():
    global high, low, secretNum, count
    count = int(math.ceil(math.log(high - low + 1)/math.log(2)))
    secretNum = random.randrange(low, high)
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global high, count
    high = 100
    print "Starting New Game with Range 0-100"
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global high, count
    high = 1000
    print "Starting New Game with Range 0-1000"
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global count, secretNum, n
    print 'Your Guess is: ' + str(guess)
    count-=1
    if int(guess)< secretNum:
        print "Guess Higher Number. " + str(count) + " chances left"
    elif int(guess)>secretNum:
        print "Guess Lower Number. " + str(count) + " chances left"
    else:
        print "Correct. You Guessed In " +str(int(n-count)) + " Chances."  
    if(count == 0):
        print 'Chances Over. Starting New Game.'
        new_game()
  
              
  
# creating frame
frame1 = simplegui.create_frame("Game", 100, 200)

#adding control elements and registering event handlers 
guess = frame1.add_input("Guess", input_guess, 200)
button1 =frame1.add_button("Range: 0 - 100", range100, 100)
button2 = frame1.add_button("Range: 0 - 1000", range1000, 100)

# starting the frame

new_game()
frame1.start()
    

