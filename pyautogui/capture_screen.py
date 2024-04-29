import pyautogui as pag 
import time

time.sleep(5)

# --------------- Capture screen ---------------
screen = pag.screenshot(region=(0, 0, 400, 400))
screen.save("img/p3.png")


