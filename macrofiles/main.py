import robloxpy
import pyautogui
import requests
import json
import numpy
import eel


print("Def Printing")

try:
    import robloxpy
    print("Module 'robloxpy' imported successfully.")
    print("RobloxPY version = 0.2.21")
except ImportError:
    print("Module 'robloxpy' is not installed. Please install it using 'pip3 install robloxpy'.")


try:
    import requests
    print("Module 'pyatogui' imported successfully.")
    print("pyatogui version = 0.9.54")
except ImportError:
    print("Module 'pyatogui' is not installed. Please install it using 'pip3 install robloxpy'.")


try:
    import json
    print("Module 'json' imported successfully.")
except ImportError:
    print("Module 'json' is not installed. Please install it using 'pip3 install json'.")\
    

try:
    import numpy
    print("Module 'numpy' imported successfully.")
except ImportError:
    print("Module 'numpy' is not installed. Please install it using 'pip3 install numpy'.")



try:
    import eel
    print("Module 'eel' imported successfully.")
except ImportError:
    print("Module 'eel' is not installed. Please install it using 'pip3 install eel'.")



screen_width, screen_height = pyautogui.size()

def smooth_move(x1, y1, x2, y2, duration):
    steps = int(duration * 100)
    for i in range(steps):
        x = x1 + (x2 - x1) * i / steps
        y = y1 + (y2 - y1) * i / steps
        pyautogui.moveTo(x, y, duration=0.01)

while True:
    start_x, start_y = pyautogui.position()
    end_x = random.randint(0, screen_width)
    end_y = random.randint(0, screen_height)
    smooth_move(start_x, start_y, end_x, end_y, duration=1)
    time.sleep(0.5)
