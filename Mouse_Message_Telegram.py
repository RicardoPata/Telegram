"""
Created on Mon May  2 23:45:53 2022

@author: RSP
github
"""

import pyautogui as pg
import time


def Message(names, message):
    i = 0
    pg.press("esc")
    time.sleep(1)
    pg.click(205,99) # search bar
    time.sleep(2)
    pg.write(names) #id names to paste
    time.sleep(2)
    pg.click(136,262) # open chat
    time.sleep(2)
    pg.click(742,678) # area to paste message
    pg.write(message) #message to paste
    time.sleep(2)
    pg.click(1153, 672) # send message
    

   

    
