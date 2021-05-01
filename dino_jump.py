# Automatizar o jogo dino no navegador
from PIL import ImageGrab, ImageOps                    
import pyautogui as pygui
import numpy as np

while True:
    x1, y1, a, b = 200, 340, 35, 50
    box = (x1, y1, x1+a, y1+b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = np.array(gray.getcolors())
    value = a.sum()
    # print(value)
    if value != 1783:
        pygui.press('space') #  Pressiona a tecla de espaço no teclado