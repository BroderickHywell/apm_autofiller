import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# the laptops we use have a resolution of 1920 x 1080

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
dft_arr = [
    'PRTR.TOD.232248843Q',
    'PRTR.TOD.2044022073Q',
    'PRTR.TOD.232248843Q'
]

closing_comments_arr = [
    'Went over to machine after I got the call and filled out the PTP. Then I got some new film and replaced it and made sure the machine was running properly. Handed it back to ops afterwards.'
]
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
THINGS TO IMPLEMENT
-time checker
-reresher
-connections closer
'''

def autofiller():
    user_input = input("---\nHej! \nPTP[1] \nRecordFiller[2]\n---\n")
    if user_input == '1':
        ptp_filler_func() #runs ptp function
    elif user_input == '2':
        record_view_filler_func()
    else:
        print('Invalid input')
        autofiller() #recurses function until user selects valid choice


def ptp_filler_func():
    user_input = input("---\nTake two[1] \nElectrical Troubleshooting[2] \nYard[3] \nPower tools[4]\n---\n")
    if user_input == '1':
        take_two_autofiller()
    elif user_input == '2':
        print('electrical troubleshooting')
    elif user_input == '3':
        print('yard')
    elif user_input == '4':
        print('power tools')   
    else:
        print('invald input')
        ptp_filler_func() # recurses function until user selects valid choice

def record_view_filler_func():
    user_input = input("---\nfilm change[1] \ndryer daily[2] \nfixation[3] \n---\n")
    if user_input == '1':
        dft_index = input('---\nWhich DFT?[1-3]\n---\n')
        if int(dft_index) > 3 or int(dft_index) < 1:
            print('invalid input')
            record_view_filler_func() #brings user back to beginning of function if an invalid input is entered
        username = input('---\nWhat is your username?\n---\n')
        downtime = input('---\nWhat is the downtime?\n---\n')
        film_change_record_filler_func(dft_index,username,downtime)
        print(dft_index)
    elif user_input == '2':
        print('dryer daily')
    elif user_input == '3':
        print('fixation')
    else:
        print('invalid input')
        record_view_filler_func() #recurses function until user selects valid choice

def film_change_record_filler_func(dft_index,username,downtime):
    #run on screen calls with data
    # print(f'dft:{dft_arr[int(dft_index)-1]}, username:{username}')

    #remove whatever is in equipment and add in the dft data, then excuse the warranty screen
    # pyautogui.sleep(4)
    pyautogui.moveTo(150, 330)
    pyautogui.click()
    pyautogui.press('backspace')
    pyautogui.write(dft_arr[int(dft_index) - 1])
    pyautogui.moveTo(50, 330)
    pyautogui.doubleClick()
    # pyautogui.sleep(4)
    pyautogui.moveTo(950, 600)
    pyautogui.doubleClick()
    pyautogui.sleep(0.5)

    #change status to in progress
    pyautogui.moveTo(900, 390)
    pyautogui.doubleClick()
    pyautogui.write('In progress')
    pyautogui.press('enter')

    #change WO execution to EXDN
    pyautogui.moveTo(850, 440)
    pyautogui.doubleClick()
    pyautogui.write('EXDN')
    pyautogui.press('enter')

    #change safety related to no
    pyautogui.moveTo(850, 460)
    pyautogui.doubleClick()
    pyautogui.write('NO')
    pyautogui.press('enter')

    #add closing comments
    pyautogui.moveTo(150, 660)
    pyautogui.doubleClick()
    pyautogui.write(closing_comments_arr[0])

    #problem code MECH/HARDWAR/MISSING
    pyautogui.moveTo(150, 680)
    pyautogui.click()
    pyautogui.write('MECH')
    pyautogui.moveTo(150, 710)
    pyautogui.click()
    pyautogui.write('HARDWAR')
    pyautogui.moveTo(150, 740)
    pyautogui.click()
    pyautogui.write('MISSING')

    #downtime
    pyautogui.moveTo(780, 605)
    pyautogui.click()
    pyautogui.moveTo(780, 635)
    pyautogui.doubleClick()
    pyautogui.write('OTHER')
    pyautogui.moveTo(780, 665)
    pyautogui.doubleClick()
    pyautogui.write('downtime')
    pyautogui.moveTo(780, 710)
    pyautogui.doubleClick()
    pyautogui.write(downtime)

    #username
    pyautogui.moveTo(1480, 605)
    pyautogui.click()
    pyautogui.write(username)
    pyautogui.moveTo(1180, 605)
    pyautogui.click()

    #checklist
    # pyautogui.moveTo(990, 450)
    # pyautogui.click()
    # pyautogui.moveTo(990, 475)
    # pyautogui.click()

    #back to record view
    # pyautogui.moveTo(50,280)





















#tester function
# film_change_record_filler_func(1,'bihowell')

def take_two_autofiller():
    pyautogui.sleep(2)
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


autofiller()