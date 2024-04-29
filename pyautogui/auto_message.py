import pyautogui as pag
import time

# --------------- Click to Chrome ---------------
pag.leftClick(1310, 1566, 1, 1)

# --------------- Delay 1 second ---------------
time.sleep(1)

# --------------- Type website URL ---------------
pag.typewrite("messenger.com")

# --------------- Press Enter ---------------
pag.press("enter")

# --------------- Click on user ---------------
pag.leftClick(390, 747, 1, 1)

# --------------- Loop over to send message ---------------
for _ in range(5):
    pag.typewrite("Hellooo")
    time.sleep(1)
    pag.press("enter")
