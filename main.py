#! /usr/bin/env python3

##############################################
# this script reads a number from the clipboard,
# does some math with it, and pastes it back
##############################################



import os
import sys
from time import sleep
import clipboard_access as win_clipboard # should be in same DIR
from threading import Thread

##########################
########## Main ##########
##########################
modified = ""

while True:
    s = ""
    number = 0.0
    try:
        s = win_clipboard.Get()
        number = float(s) * 3.0 / 5.0
    except (TypeError, ValueError):
        # the contents of the clipboard isn't text or isn't a number
        s = ""
        modified = ""
        sleep(1)
    
    if s != modified:
        modified = "{:03.2f}".format(number)
        print(s, "->", modified)
        win_clipboard.Paste(modified)
    
    sleep(0.1)

    
    
    

