"Stopwatch: The Game"

import simplegui

# global variables
global timer, trials
clock = 0
trials = 0
wins = 0

# helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global clock
    minutes = clock // 600
    seconds = (clock % 600) // 10
    tens_of_seconds = seconds // 10
    ones_of_seconds = seconds % 10
    tenths_seconds = (clock % 600) % 10
    time = str(minutes) + ":" + str(tens_of_seconds) + str(ones_of_seconds) +"." + str(tenths_seconds)
    return time
    
def score():
    global trials, wins
    score = str(wins) + "/" + str(trials)
    return score
    
# event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timer, clock
    timer.start() 

def stop_handler():
    global timer, trials, wins
    timer.stop()
    trials = trials + 1
    if (clock % 10) == 0:
        wins = wins + 1
    
def reset_handler():
    global clock, trials, wins
    stop_handler()
    clock = 0
    trials = 0
    wins = 0
   

# event handler for timer with 0.1 sec interval
def timer_handler():
    global clock
    clock = clock + 1
    

#  draw handler
def draw_handler(canvas):
    canvas.draw_text(format(), [100, 150], 45, 'Red')
    canvas.draw_text(score(), [200, 50], 30, 'White')
    
# frame
f = simplegui.create_frame ("Stopwatch Game", 300, 300)

# event handlers
f.add_button ("Start", start_handler, 100)
f.add_button ("Stop", stop_handler, 100)
f.add_button ("Reset", reset_handler, 100)
f.set_draw_handler(draw_handler)

# start frame
timer = simplegui.create_timer(100, timer_handler)
f.start()

