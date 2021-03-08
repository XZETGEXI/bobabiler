from random import random, choice, choices, randint, shuffle

import os, time, math, string

W, H = os.get_terminal_size()

MSG_TIMING = 4
POSTER_TIMING = 4
NAME_LEN = 6
MSG_LEN = W // 2 - 4
TEXT_WHITESPACES = 8
DOT_ENDING_PROBABILITY = 10
MAX_SENTENCES = 5


NUMBERS = [f'{i}' for i in range(10)]
END_CHARACTERS = ["?", " !", "...", " ^_^"] + ["."] * DOT_ENDING_PROBABILITY


def rad_rand(n = 1):
    assert n <= 18014398509481982
    
    try:
        return (int(random() * 100) % n) + 1
    except:
        return 0


def get_dateclock():
    dates = [rad_rand(31), rad_rand(12), 2000 + rad_rand(21)]
    dates = [str(date) for date in dates]
    date = "/".join(dates)

    clocks = [rad_rand(24) - 1, rad_rand(60 - 1)]
    clocks = [str(clock) for clock in clocks]
    clock = ":".join(clocks)
        
    dateclock = date + " | " + clock
    return dateclock


def get_name():
    name_length = rad_rand(NAME_LEN)

    name = []
    for i in range(name_length):
        name.append(chr(rad_rand(200) + 12036))

    name = "".join(name)
    name = "[" + name + "]"
    
    return name
    
    
def get_msg():
    msg_length = rad_rand(MSG_LEN)

    msg = []
    for i in range(msg_length):
        msg.append(chr(rad_rand(200) + 12036))
            
    msg += [" "] * rad_rand(TEXT_WHITESPACES)
    shuffle(msg)
    msg = "".join(msg)
    msg = msg.strip()
    msg = "> " + msg
    msg = msg + choice(END_CHARACTERS)
        
    return msg


def pause(timing):
    sleep_time = rad_rand(MSG_TIMING)
    time.sleep(math.sqrt(sleep_time))


def main():
    while True:
        
        dateclock = get_dateclock()
        print(dateclock.rjust(W, " "))
        
        name = get_name()
        print(name)
        
        sentences = rad_rand(MAX_SENTENCES)
        for sentence in range(sentences):
            msg = get_msg()
            print(msg)
            
            pause(MSG_TIMING)
            
        pause(POSTER_TIMING)
        
        

main()
