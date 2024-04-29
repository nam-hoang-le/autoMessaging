import pyautogui as pag 
import time 

# --------------- Delay screen ---------------
time.sleep(5)

# --------------- Find the objects ---------------
img = 'img/chrome_refresh.png'

# --------------- Find the image and click ---------------
img_find = pag.locateOnScreen(img)
pag.click(img_find)

