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


'''
#RECORD VIEW AUTOMATION
pyautogui.sleep(2)
pyautogui.moveTo(300, 650)
pyautogui.doubleClick()
pyautogui.write('Hello world!')
pyautogui.moveTo(300, 680)


def my_function():
  print("Hello from a function")

THINGS TO IMPLEMENT
-time checker
-reresher
'''

def autofiller():
    user_input = input("Hej! PTP[1] or RecordFiller[2]?")
    if user_input == '1':
        print("ptp")
        ptp_filler_func()
    elif user_input == '2':
        print('recordview')
    else:
        print('Invalid input')
        autofiller() #recurses function until user selects valid choice


def ptp_filler_func():
    user_input = input("Take two[1] \nElectrical Troubleshooting[2] \nYard[3] \nPower tools[4]")
    if user_input == '1':
        print('take two')
    elif user_input == '2':
        print('electrical troubleshooting')
    elif user_input == '3':
        print('yard')
    elif user_input == '4':
        print('power tools')   
    else:
        print('invald input')
        ptp_filler_func() # recurses function until user selects valid choice
    


autofiller()


'''
# PTP TAKE 2 AUTOMATION
pyautogui.sleep(1)
# selects ptp from tab
pyautogui.moveTo(450, 270)
pyautogui.doubleClick()
pyautogui.sleep(6) # this one goes longer than normal because sometimes there are delays with the network
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
pyautogui.sleep(3)
# # second checkbox
pyautogui.moveTo(60, 950)
pyautogui.click()
pyautogui.scroll(-500)
pyautogui.moveTo(1800, 935)
pyautogui.doubleClick()
pyautogui.sleep(3)
# # third checkbox
pyautogui.moveTo(60, 950)
pyautogui.click()
pyautogui.scroll(-500)
pyautogui.moveTo(1800, 935)
pyautogui.doubleClick()
pyautogui.sleep(3)
# submit form
pyautogui.scroll(-1200)
pyautogui.moveTo(1800, 932)
pyautogui.doubleClick()
'''
