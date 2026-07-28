'''
author: yvonne
function: build a timer for studying, manage your time, take a long term focus, then have a little break
'''

def ask_user_mode():
    time_mode = [1, 2, 3, 4]
    print("Time mode: \n" \
            "1: Focus 25 minutes, break 5 minutes \n" \
            "2: Focus 50 minutes, break 10 minures \n" \
            "3: Focus 100 miuntes, break 15 minutes \n" \
            "4: Focus 150 minutes, break 25 minutes")
    user_choose_mode = int(input("Enter the time mode: "))
    while user_choose_mode not in time_mode:
        user_choose_mode = int(input("Please choose a valid mode!"))
    print("You choose mode {} !".format(user_choose_mode))
    return user_choose_mode
ask_user_mode()