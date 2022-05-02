#this code is made by Amara Hemanth Kumar
from pynput.keyboard import Key, Controller 
import time 
print("Make the tab where you wanted to auto type conviniently to reach with minimam clicks \n")
L=input("Enter file location:")
a = open(L,'r')
print(" \n CATION!!! please do not interfer with mouse while auto typing \n")
print("Now your system is ready to type. \n")
print("Please click the mouse cursor where you wanted to type. \n ")
keyboard= Controller()  
def split(words):  
    return[char for char in words] 
time.sleep(20) 
for i in split(a): 
    keyboard.type (i)  
    time.sleep(.1)
a.close()