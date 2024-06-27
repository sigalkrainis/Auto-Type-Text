import pyautogui
import time


inputString = input("Enter your String:")
time.sleep(3)
pyautogui.typewrite(inputString, interval= 0.05)
   