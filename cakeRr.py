#!/usr/bin/env python3

# Script to make working with cakeHr faster
# w to enter weekday, f friday, e to pass to the next day
# esc to quit

import pyautogui as pa
from pynput import keyboard
import time

pa.PAUSE=0.05
pa.FAILSAFE = True

# Enter your hours here
weekHours={'start': '0800', 'end': '1800', 'pause': '0100'}
friHours={'start': '0800', 'end': '1800', 'pause': '0100'}

def enterDay(hours):
    pa.click();
    pa.write(hours['start'])
    
    pa.moveRel(75,0)
    pa.click();
    pa.write(hours['end'])
    
    pa.moveRel(75,0)
    pa.click();
    pa.write(hours['pause'])
    
    pa.moveRel(360,0)
    pa.click();
    
    pa.moveRel(-510,0)
    time.sleep(1)

def passDay():
	pa.scroll(-1)
	pa.moveRel(0,12)

	
    
def on_press(key):
    try:
        if key.char == 'w':
            enterDay(weekHours)
        if key.char == 'f':
            enterDay(friHours)
        if key.char == 'e':
            passDay()
            
    except AttributeError:
        print ('cakeRr: press esc to quit')
    
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
with keyboard.Listener(on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
