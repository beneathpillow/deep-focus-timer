'''
author: yvonne
function: build a timer for studying, manage your time, take a long term focus, then have a little break
'''

time_mode = [1, 2, 3, 4]
time_mode_detail = {
    1:(25, 5),
    2:(50, 10), 
    3:(100, 15), 
    4:(150, 25)
    }


def ask_user_mode():
    print("Time mode: \n" \
            "1: Focus 25 minutes, break 5 minutes \n" \
            "2: Focus 50 minutes, break 10 minures \n" \
            "3: Focus 100 miuntes, break 15 minutes \n" \
            "4: Focus 150 minutes, break 25 minutes")

    user_choose_mode = None

    while user_choose_mode not in time_mode:
        try:
            user_choose_mode = int(input("Please choose a valid mode! "))
            if user_choose_mode not in time_mode:
                print("Please choose a number from 1 to 4.")
        except ValueError:
            print("Please enter a number. ")
    
    print("You choose mode {} !".format(user_choose_mode))
    return user_choose_mode

def get_time_mode(user_choose_mode):
    focus_time, break_time = time_mode_detail[user_choose_mode]
    return focus_time, break_time

def convert_time_mode_second(focus_time, break_time):
    focus_time = focus_time * 60
    break_time = break_time * 60
    return focus_time, break_time



def main():
    user_choose_mode = ask_user_mode()
    focus_time, break_time = get_time_mode(user_choose_mode)
    focus_second, break_second = convert_time_mode_second(focus_time, break_time)
    print("Focus time: {} minutes".format(focus_time))
    print("Break time : {} minutes".format(break_time))
    print(focus_second, break_second)
main()
