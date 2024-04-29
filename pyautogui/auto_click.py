import pyautogui as pag 
import time 

# --------------- Stop the program ---------------
time.sleep(5)

# --------------- Take position mouse ---------------
pos = pag.position()

# --------------- Auto click ---------------
# --------------- Loop over the program
for _ in range(3):
    pag.click(pos)
    time.sleep(2)


