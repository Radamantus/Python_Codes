from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import*


while True:
    x1, y1, a, b = 200, 340, 35, 50
    box = (x1, y1, x1+a, y1+b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = array(gray.getcolors())
    value = a.sum()
    # print(value)
    if(value != 1783):pyautogui.press('space')