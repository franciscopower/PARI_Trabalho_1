#!/usr/bin/python

# Imports
from collections import namedtuple
from time import time
import argparse


def test_line():
    pass



def statistics(inputs):
    """
    Create Statistics dictionary
    :param value: list of named tuples with test results
    :return: dictionary of statistics
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
    
    cond = False #substitute with condition according to the parsed inputs
    
    while cond:
        test_line()
        





if __name__== "__main__":
    main()