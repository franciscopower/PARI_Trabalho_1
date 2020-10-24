#!/usr/bin/python
#-------------------------------
#Writing test with number of letters to test or time limit
#group number 5
#PARI, October 2020


# Imports
from collections import namedtuple
import time
from random import randint
from colorama import Fore, init
import argparse
import readchar
from datetime import datetime
from pprint import pprint

#initialize colorama
init(autoreset = True)

#stop test bool
stop_test = False

# declare named tuple
Result = namedtuple('Result', ['requested','received','time'])

#week days
week = ('Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun')

# -------------------------------------------------------------------

def test_line():
    """
    Requests a char and evaluates the input. Also times the operation
    
    Return: named tuple with requested_char, input_char and dt (delta time)
    """
    global stop_test
    
    r = randint(97,122)
    requested_char = chr(r)
    print("Please type the letter " + Fore.BLUE + requested_char)
    tic = time.time()
    input_char = readchar.readchar()
    toc = time.time()
    dt = toc - tic
    
    if input_char == " ":
        stop_test = True
        print(Fore.RED + '\n--ATTENTION--')
        print("You interrupted your test.")
        return
    
    #use colorama to write output
    if requested_char == input_char:
        print("You typed the letter " + Fore.GREEN + input_char)
    else:
        print("You typed the letter " + Fore.RED + input_char)
    
    # place requested_char, input_char and dt (delta time) in named tuple
    return Result(requested=requested_char, received=input_char, time=dt)
    
 # ----------------------------------------------------------------   
    
def time_mode(max_time):
    """Runs test line for a specific amount of time

    Args:
        t (int): time to run test
    Return: 
        all_results (list): list of tupples with results from all tests
    """
    global stop_test
    
    all_results = []
    
    tic = time.time()
    dt = 0
    
    while dt < max_time:
        t = test_line()
        if stop_test:
            break
        all_results.append(t)
        toc = time.time()
        dt = toc - tic
        
    if dt > max_time:
        print('\nTest duration was of ' + str(dt) + ' seconds, more than the maximum ' + str(max_time) + ' seconds.')
        
        
    return all_results
        
    
# ----------------------------------------------------------       
        
def iter_mode(N):
    """Runs test line a chosen number of times

    Args:
        N (int): number o times to run test
    Return: 
        all_results (list): list of tupples with results from all tests
        
    """
    global stop_test
    
    all_results = []
    for _ in range(N):
        t = test_line()
        if stop_test:
            break
        all_results.append(t)
                
    return all_results

def statistics(main_results, start_time, end_time):
    """Create Statistics dictionary
    
    Args: 
        main_results (list): list of named tuples with test results
        start_time (string): time of test begin
        end_time (string): time of test end

    Return: dictionary of statistics
    """

    right = 0 #number o right charecters
    wrong = 0 #number o wrong charecters
    r_time = 0 #total time of right charecters
    w_time = 0 #total time of wrong charecters
    
    for t in main_results:
        if t[0] == t[1]:
            right += 1
            r_time += t[2]
        else:
            wrong += 1
            w_time += t[2]
            
    #Calculate number o types
    number_of_types = right + wrong #same as len(main_results)
    
    #Calculate total time
    total_time = r_time + w_time

    #Calculate type average duration
    if (right + wrong) == 0:
        type_average_duration = 0
        accuracy2 = 0
    else:
        type_average_duration = (r_time + w_time)/(right + wrong)
        #calculate accuracy
        accuracy2 = float(right)/(float(right+wrong)) # multiply by 100 if expressend iin %
    
     #calculate type hit average duration
    if right == 0:
        type_hit_average_duration = 0
    else:
        type_hit_average_duration = r_time/right

    #calculate type miss average duration
    if wrong == 0:    
        type_miss_average_duration = 0
    else:
        type_miss_average_duration = w_time/wrong
     

    return {
        'accuracy': accuracy2,
        'inputs':  main_results,
        'number_of_hits': right,
        'number_of_types': number_of_types,
        'test_duration': total_time,
        'test_end': end_time,
        'test_start': start_time,
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration,
    }
    
# -------------------------------------------------------------

def main():
    """test_line()
    Typing test
    """

    # Parsing. 
    parser = argparse.ArgumentParser(description = "Definition of test mode")
    parser.add_argument('-utm', '--user_time_mode', action='store_true', help = 'If used, test will be time based.')
    parser.add_argument('-mv', '--max_value', help = 'Max number of secs for time mode or maximum number of inputs for number of inputs mode.', required=True)
    
    args = parser.parse_args()
    
    mode = args.user_time_mode
    maxi = int(args.max_value)
    
    print('-------------------------------------------------------------------')
    print('PARI typing test.')
    print('Francisco Power, Miguel Carvalhais, Rita Correia, October of 2020')
    print('-------------------------------------------------------------------\n')
    
    if mode:
        print('Your test will last ' + str(maxi) + ' seconds.')
    else:
        print('You will have to type ' + str(maxi) + ' charecters.')
    
    print("Press any key to start the test.\n")
    _ = readchar.readchar()
        
    now = datetime.now()
    start_time = now.strftime("%b %d %H:%M:%S %Y")
    start_time = week[now.weekday()] + ' ' + start_time
        
    if mode:
        main_results = time_mode(maxi)
    else:
        main_results = iter_mode(maxi)
    
    now = datetime.now()
    end_time = now.strftime("%b %d %H:%M:%S %Y")
    end_time = week[now.weekday()] + ' ' + end_time
    
    print(Fore.BLUE + '\nThe test ended.\n')

    #print the results of the statistic function with the parameters: main_results,start_time and end_time
    pprint(statistics(main_results, start_time, end_time))

    
    print('\nThanks for playing!')
    print('-------------------------------------------------------------------\n')


if __name__ == "__main__":
    main()