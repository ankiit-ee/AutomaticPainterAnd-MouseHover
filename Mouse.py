import pyautogui

# Depending on your program pyautogui can go rogue so we use a fail safe
pyautogui.FAILSAFE = True

# Location is provided as x,y pair
# Depends on resolution of the Monitor
# Can obtain the resolution
# print(pyautogui.size())   // Size(width=1920, height=1080)

# Moving the mouse to a specific location
# pyautogui.moveTo(100, 100, duration=0.25)

# Move the mouse in a loop
# for i in range(10):
#     pyautogui.moveTo(100,100,duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

