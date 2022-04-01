import time
import random
import pyautogui
 
def move_mouse(timeset):
    start_time = time.time()
    timeslp = time.time() - start_time
    xsize, ysize = pyautogui.size()
    
    while timeslp < timeset:
        x, y = random.randrange(xsize), random.randrange(ysize)
        pyautogui.moveTo(x, y, duration=0.02)
        timeslp = time.time() - start_time
 
if __name__ == "__main__":
    pyautogui.alert("Update Completed")
    move_mouse(15)