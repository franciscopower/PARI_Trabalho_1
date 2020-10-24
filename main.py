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

#initialize colorama
init(autoreset = True)

# declare named tuple
Result = namedtuple('Result', ['requested','received','time'])

# -------------------------------------------------------------------

def test_line():
    """
    Requests a char and evaluates the input. Also times the operation
    
    Return: named tuple with requested_char, input_char and dt (delta time)
    """
    
    r = randint(97,122)
    requested_char = chr(r)
    print("Please type the letter " + Fore.BLUE + requested_char)
    tic = time.time()
    input_char = readchar.readchar()
    toc = time.time()
    dt = toc - tic
    
    #use colorama to write output
    if requested_char == input_char:
        print("You typed the letter " + Fore.GREEN + input_char)
    else:
        print("You typed the letter " + Fore.RED + input_char)
    
    # place requested_char, input_char and dt (delta time) in named tuple
    return Result(requested=requested_char, received=input_char, time=dt)
    
 # ----------------------------------------------------------------   
    
def time_mode(t):
    """Runs test line for a specific amount of time

    Args:
        t (int): time to run test
    Return: 
        all_results (list): list of tupples with results from all tests
    """
    all_results = []
    n=0
    
    tic = time.time()
    dt = 0
    
    while dt < t:
        all_results[n] = test_line()
        toc = time.time()
        dt = toc - tic
        n += 1
        
    return all_results
        
    
# ----------------------------------------------------------       
        
def iter_mode(N):
    """Runs test line a chosen number of times

    Args:
        N (int): number o times to run test
    Return: 
        all_results (list): list of tupples with results from all tests
        
    """
    all_results = []
    for n in range(N):
        all_results[n] = test_line()
        
    return all_results

# -----------------------------------------------------------

def statistics(main_results, start_time, end_time):
    """Create Statistics dictionary
    
    Args: 
        main_results (list): list of named tuples with test results
        start_time (string): time of test begin
        end_time (string): time of test end

    Return: dictionary of statistics
    """

    right = 0 #number o right charecters
    wrong = 0 #number o wrong  charecters
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
    type_average_duration = (r_time + w_time)/(right + wrong)

    #calculate type hit average duration
    type_hit_average_duration = r_time/right

    #calculate type miss average duration
    type_miss_average_duration = w_time/wrong
    
    #calculate accuracy
    accuracy = right/(right+wrong) # multiply by 100 if expressend iin %

    return {
        'accuracy': accuracy,
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
    """
    Typing test
    """

    # Parsing. 
    parser = argparse.ArgumentParser(description = "Definition of test mode")
    parser.add_argument('-utm', '--user_time_mode', action='store_true', help = 'If used, test will be time based.')
    parser.add_argument('-mv', '--max_value', help = 'Max number of secs for time mode or maximum number of inputs for number of inputs mode.', required=True)
    
    args = parser.parse_args()
    
    mode = args.user_time_mode
    maxi = args.max_value
    
    print(mode)
    print(maxi)
    
    print("Press any key to start")
    start = readchar.readchar()
        
    now = datetime.now()
    start_time = now.strftime("%b %d %H:%M:%S %Y")
        
    if mode:
        main_results = time_mode(maxi)
    else:
        main_results = iter_mode(maxi)
        
    now = datetime.now()
    end_time = now.strftime("%b %d %H:%M:%S %Y")

    #print the results of the statistic function with the parameters: main_results,start_time and end_time
    print(statistics(main_results, start_time, end_time))
