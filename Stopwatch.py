# "Stopwatch: The Game"
# created by Prerna Satija
import simplegui

# global variables

timeinsec=0
stop_flag = True
D = 0
totalcount = 0
successcount = 0

# time in the format A:BC.D

def format(t):
    global D
    D = t % 10
    sec = (t-D)/ 10
    A = 0
    C = 0 
    if(sec>=60):
        C = sec % 60
        A = (sec - C)/60
    if(sec<10):
        sec = '0' + str(sec)
    return str(A) + ":" + str(sec) + "." + str(D)
     
    
# Event handlers for buttons; "Start", "Stop", "Reset"
# start
def button_handler1():
    timer.start()
# stop    
def button_handler2():
    global D, totalcount, successcount
    if timer.is_running():
        totalcount += 1
        if D==0:
            successcount += 1
    timer.stop()
    stop_flag = False   

# reset
def button_handler3():
    global timeinsec, successcount, totalcount
    successcount = 0
    totalcount = 0
    timeinsec = 0
    timer.stop()
    
# stop count game score
def score():
    global totalcount, successcount
    return str(successcount) + "/" + str(totalcount)

# event handler for timer

def updatetime():
    global timeinsec
    timeinsec = timeinsec + 1

# draw handler

def draw(canvas):
    canvas.draw_text(str(format(timeinsec)), (150, 150), 32, "White")
    format(timeinsec)
    canvas.draw_text(score(), (250, 50), 20, "Red")
    
# created frame and timer

f = simplegui.create_frame("stopwatch", 300, 300)
timer = simplegui.create_timer(100, updatetime)

start_button = f.add_button("Start", button_handler1, 100)
stop_button = f.add_button("Stop", button_handler2, 100)
reset_button = f.add_button("Reset", button_handler3, 100)

f.set_draw_handler(draw)

f.start()



