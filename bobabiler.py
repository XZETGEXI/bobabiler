from random import random, choice, choices, randint, shuffle

from kanji_lists import JOYO

import os, time, math

W, H = os.get_terminal_size()

NUMBERS = [f'{i}' for i in range(10)]

CHARACTERS = [*JOYO]

END_CHARACTERS = ["?", " !", "...", " ^_^"] + ["."] * 10

def rad_rand(n = 1):
    assert n <= 18014398509481982
    
    try:
        return (int(random() * 100) % n) + 1
    except:
        return 0


def main():
    
    while True:
        
        dates = [rad_rand(31), rad_rand(12), 2000 + rad_rand(21)]
        dates = [str(date) for date in dates]
        date = "/".join(dates)
        
        clocks = [rad_rand(25) - 1, rad_rand(60 - 1)]
        clocks = [str(clock) for clock in clocks]
        clock = ":".join(clocks)
        
        dateclock = date + " | " + clock
        
        print(dateclock.rjust(W, " "))
        
        name_length = rad_rand(6)
        name = "".join(choices(CHARACTERS, k = name_length))
        name = "[" + name + "]"
        
        print(name)
        
        sentences = rad_rand(5)
        for sentence in range(sentences):
            
            msg_length = rad_rand(40)
            msg = choices(CHARACTERS, k = msg_length)
            msg += [" "] * rad_rand(4)
            shuffle(msg)
            msg = "".join(msg)
            msg = msg.strip()
            msg = "> " + msg
            msg = msg + choice(END_CHARACTERS)
            
            print(msg)
        
            sleep_time = rad_rand(4)
            time.sleep(0.1 * sleep_time)
    
        sleep_time = rad_rand(4)
        time.sleep(math.log(1.1 * sleep_time))
        
        print()

      
main()
