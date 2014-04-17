# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui


frame = simplegui.create_frame("shape", 300, 300)

def draw(canvas):
    canvas.draw_circle([90, 200], 20, 10, 'white')
    canvas.draw_circle([210, 200], 20, 10, 'white')
    canvas.draw_line([50,180], [250,180], 40, 'red')
    canvas.draw_line([55,170], [90,120], 5, 'red')
    canvas.draw_line([90,120], [130,120], 5, 'red')
    canvas.draw_line([180,108], [180,160], 140, 'red')
    


#draw handler
frame.set_draw_handler(draw)

frame.start()