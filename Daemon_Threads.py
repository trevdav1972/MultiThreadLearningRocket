import threading 
import time 

path = "text.txt"
text = ""

def readfile():
    global path, text
    while True: 
        with open("Text.txt", "r") as f: 
            text = f.read()
        time.sleep(3)
def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)