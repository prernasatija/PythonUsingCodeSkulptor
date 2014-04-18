#Collatz conjecture


import simplegui
import math

# global variables  
s1 = ''

def calculateNext(n):
    global next,s1
    if n % 2 == 0:
        next = n/2
    else:
        next = 3*n + 1
    #print next
    s1 = s1 + ' ' + str(next)

def update():
    global next,s1
    if next == 1:
        timer1.stop()
        print s1
    else:
        calculateNext(next)     
    
# create timer

timer1 = simplegui.create_timer(1, update)

calculateNext(217)
timer1.start()


