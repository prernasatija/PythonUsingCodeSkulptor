# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    if name=="rock": 
        num = 0
    elif name == "Spock":
        num = 1
    elif name == "paper":
        num = 2
    elif name == "lizard":
        num = 3
    elif name == "scissors":
        num = 4
    else:
        print "Error: No number for this name."
        num = 1000
    return num

def number_to_name(number):
    if number==0: 
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        name = "Error: No name corresponding to this number."
        print name
    return name
    
# main function
def rpsls(player_choice): 
    print "\n"
    print "Player chooses "+ player_choice
    player_number = name_to_number(player_choice)
    #generates a random number that can range from 0 to 5 excluding 5
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)  
    print "Computer chooses " + comp_choice
    diff  = (comp_number - player_number)%5
    if (diff==1) or (diff==2):
        print "Computer wins!"
    elif (diff==3) or (diff==4):
        print "Player wins!"
    else: 
        print "Player and computer tie!"
    

#testing        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
