import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# the laptops we use have a resolution of 1920 x 1080

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

# pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

# pyautogui.click()          # Click the mouse.
# pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.

# pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

# pyautogui.doubleClick()
# pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
# with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
#     pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# Shift key is released automatically.
# pyautogui.alert(f"screen width{screenWidth}, screen height{screenHeight}") # Make an alert box appear and pause the program until OK is clicked.

# References
# pyautogui.hotkey('ctrl', 'c') Press the Ctrl-C hotkey combination.
# pyautogui.click('button.png') Find where button.png appears on the screen and click it.
# pyautogui.doubleClick()      Double click the mouse.


# record view automation
'''
pyautogui.sleep(2)
pyautogui.moveTo(300, 650)
pyautogui.doubleClick()
pyautogui.write('Hello world!')
pyautogui.moveTo(300, 680)
'''

# PTP TAKE 2 AUTOMATION

# selects ptp from tab
pyautogui.moveTo(450, 270)
pyautogui.doubleClick()
pyautogui.sleep(2)
# # selects create assessment
pyautogui.moveTo(1700, 670)
pyautogui.doubleClick()
pyautogui.sleep(2)
# # first checkbox
pyautogui.moveTo(60, 870)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.moveTo(1830, 895)
pyautogui.doubleClick()
pyautogui.sleep(2)
# # second checkbox
pyautogui.moveTo(60, 950)
pyautogui.click()
pyautogui.scroll(-500)
pyautogui.moveTo(1800, 935)
pyautogui.doubleClick()
pyautogui.sleep(2)
# # third checkbox
pyautogui.moveTo(60, 950)
pyautogui.click()
pyautogui.scroll(-500)
pyautogui.moveTo(1800, 935)
pyautogui.doubleClick()
pyautogui.sleep(2)
# submit form
pyautogui.scroll(-1200)
pyautogui.moveTo(1800, 932)
pyautogui.doubleClick()



