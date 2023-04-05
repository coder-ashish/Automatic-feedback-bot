#/
#    author:   coder-ashish
#    created:  04.04.2023 21:23:38
#/

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def pressTab():
    keyboard.press(Key.tab)
    time.sleep(0.1)
    keyboard.release(Key.tab)
    time.sleep(0.1)

def pressDown():
    keyboard.press(Key.down)
    time.sleep(0.1)
    keyboard.release(Key.down)
    time.sleep(0.1)

def fill_feedback():
    pressDown()
    time.sleep(2)
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressTab()

print("Get ready, and point your cursor at the first index position...")
time.sleep(3)

while(True):
    fill_feedback()
