pyClipboardModifier
===================

Listens for changes in the Windows clipboard and modifies the contents automatically.


Lets say you have many values to adjust in the same fassion. Sometimes writing 
a script to modify the values isn't worth it (because it's complex or because 
there's few values to adjust). With this script running you simply highlight 
the value, hit Ctrl + C, the script sees the new value in the clipboard and 
modifies it according to the code, you paste the new value. Anyone watching 
you do this would be very confused. 



Example Usage: you have several assignment marks all out of 30 and you want to 
convert each to a percentage. You'd adjust the code to take the clipboard 
value, divid it by 30 to get your percentage, and put it back in the clipboard. 