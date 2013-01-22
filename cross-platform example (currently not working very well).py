#! /bin/python

from tkinter import Tk
from tkinter import TclError
from time import sleep


#############################
######### start code ########
#############################
modified = ""
while True:
	r = Tk()
	r.withdraw()
	s = ""
	try:
		s = r.clipboard_get()
	except (TclError):
		#print("Caught Error")
		pass
	
	print(s)
	
	if s != modified:
		s += " - Modified"
		modified = s
		r.clipboard_clear()
		r.clipboard_append(modified)
		print("string modified:", s)
		#exit()
	
	#r.destroy()
	
	sleep(0.75)