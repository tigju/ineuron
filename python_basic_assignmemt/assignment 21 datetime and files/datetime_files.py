import datetime
import os
from multiprocessing import Process
import time
import random

# for processes to work correctly, finction has to be defined outside the main
# or imported from different file.
# define function for multiprocessing
def print_time():
    wait_time = random.choice(range(1, 5))
    time.sleep(wait_time)
    print(f"Wait time: ", wait_time, " seconds. Current time:", time.ctime())

if __name__ == '__main__':

    ### 1 ###
    today = datetime.date.today()
    with open("today.txt", 'w') as f:
        f.write(str(today))
    # ### ###

    # ### 2 ###
    with open("today.txt", 'r') as f:
        date_string = f.read()
    # ### ###

    # ### 3 ###
    parsed_date = datetime.date.fromisoformat(date_string)
    print("Parsed date object: ", parsed_date)
    # ### ###

    # ### 4 ###
    curr_dir = os.listdir('.')
    print("current directory: ", curr_dir)
    # # ### ###

    # # ### 5 ###
    parent_dir = os.listdir('..')
    print("parent directory: ", parent_dir)
    # ### ###

    ### 6 ###

    process1 = Process(target=print_time)
    process2 = Process(target=print_time)
    process3 = Process(target=print_time)

    process1.start()
    process2.start()
    process3.start()
    # wait untill 3 processes are done
    process1.join()
    process2.join()
    process3.join()
    print("Processes are done!")
    ### ###

    ### 7 ###
    dob = datetime.datetime(1986, 11, 24)
    print("Date of Birth: ", dob)
    # ### ###

    # ### 8 ###
    print("Day of the week: ", dob.strftime('%A'))
    # ### ###

    # ### 9 ###
    ten_thousand_days_old = dob + datetime.timedelta(days=10000)
    print("10,000 years old was: ", ten_thousand_days_old)
    ### ###
