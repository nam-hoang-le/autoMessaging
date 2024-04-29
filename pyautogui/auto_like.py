import pyautogui as pag 
import time 

# --------------- Stop the program ---------------
time.sleep(5)


for _ in range(5): 
    pos_1 = pag.position(916, 471)
    pag.doubleClick(pos_1)
    time.sleep(2)
    pos_2 = pag.position(1616, 849)
    pag.click(pos_2)
    time.sleep(2)