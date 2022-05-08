# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:45:53 2022

@author: RSP
github
"""

from Mouse_Message_Telegram import Message
import pyautogui as pg
import time

Symbols = []

with open("TelegramNames.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        Symbols.append(line) #storing everything in memory!
file.close()
time.sleep(5)

Message_A = '''Message A - change this text'''
size = len(Symbols)

def Post():        
    for each_name in Symbols:    
            Message(each_name,Message_A)
            time.sleep(10)
            
Post()
        
    