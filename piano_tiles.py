from pyautogui import *
import pyautogui
import time
import keyboard
from keyboard import press_and_release as pr
import win32api 
import win32con
import webbrowser  # opens websites using open( )

# pyautogui.mouseInfo()

21,45,86
tile1x,tile1y=297,600
tile2x,tile2y=422,600
tile3x,tile3y=534,600
tile4x,tile4y=650,600

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
result='https://lagged.com/en/g/piano-tiles-3'
keyboard.send("windows+right")
sleep(0.5)
webbrowser.get('chrome').open(result)


def click(x,y) :
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
print('running')

while keyboard.is_pressed('q') == False :

     if pyautogui.pixel(tile1x,tile1y) [0] <=25:
        click(tile1x,tile1y)
        # time.sleep(0.01)

     if pyautogui.pixel(tile2x,tile2y) [0] <= 25:
        click(tile2x,tile2y)
        # time.sleep(0.01)

     if pyautogui.pixel(tile3x,tile3y) [0] <= 25:
        click(tile3x,tile3y)
        # time.sleep(0.01)

     if pyautogui.pixel(tile4x,tile4y) [0] <= 25:
        click(tile4x,tile4y)
        
       
