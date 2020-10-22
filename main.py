#!/usr/bin/python
#-------------------------------
#Writing test with number of letters to test or time limit
#group number 5
#PARI, October 2020


# Imports
from collections import namedtuple
import time
from random import randint
import colorama
import argparse
import readchar


# declare named tuple
Result = namedtuple('Result', ['requested','received','time'])

def test_line():
    """
    Requests a char and evaluates the input. Also times the operation
    
    Return: named tuple with requested_char, input_char and dt (delta time)
    """
    
    r = randint(97,122)
    requested_char = chr(r)
    # write request as print("Write an " + requested_char)
    tic = time.time()
    input_char = readchar.readchar()
    toc = time.time()
    dt = toc - tic
    
    #use colorama to write output
    if requested_char == input_char:
        pass #print result in green
    else:
        pass #print result in red
    
    # place requested_char, input_char and dt (delta time) in named tuple
    return Result(requested=requested_char, received=input_char, time=dt)
    
    
    
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
        
    
        
        
def iter_mode(N):
    """Runs test line a chosen number of times

    Args:
        N (int): number o times to run test
    Return: 
        all_results (list): list of tupples with results from all tests
        
    """
    all_results = []
    for n in range(N):
        all_results(n) = test_line()
        
    return all_results


def statistics(inputs):
    """Create Statistics dictionary
    
    Args: 
        inputs (list): list of named tuples with test results
    Return: dictionary of statistics
    """

    #calculate Time
    test_start = time.time()
    test_end = time.time()
    test_duration = test_end - test_start


    #calculate accuracy
    accuracy="0"
    number_of_hits=0
    count=0
    for i,c in enumerate(request_char):
        try:
            if input_char[i]==c:
                count +=1
        except:
            pass
    accuracy=float((count/request_char)*100)

    #calculate Number of hits
      pass #sera o contador, porque accuracy e o numero de hits /total


    #Calculate type average duration
    type_average_duration=0

    #calculate type hit average duration
    type_hit_average_duration=0

    #calculate type miss average duration
    type_miss_average_duration=0







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
        
    if mode:
        main_results = time_mode(maxi)
    else:
        main_results = iter_mode(maxi)
        
    print(statistics(main_results))
        
        

if __name__== "__main__":
    main()