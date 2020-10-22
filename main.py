#!/usr/bin/python

# Imports
from collections import namedtuple
import time
from random import randint
import colorama
import argparse
import readchar


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
    
    
    
def time_mode(t):
    """Runs test line for a specific amount of time

    Args:
        t (int): time to run test
    """
    
    tic = time.time()
    dt = 0
    while dt < t:
        test_line()
        toc = time.time()
        dt = toc - tic
        
        
def iter_mode(N):
    """Runs test line a chosen number of times

    Args:
        N (int): number o times to run test
    """
    for n in range(N):
        test_line()


def statistics(inputs):
    """Create Statistics dictionary
    
    Args: 
        inputs (list): list of named tuples with test results
    Return: dictionary of statistics
    """
    pass



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
        time_mode(maxi)
    else:
        iter_mode(maxi)
        
        
        
        

if __name__== "__main__":
    main()