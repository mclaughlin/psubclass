#!/usr/bin/env python3

"""
Simple script to output (in a pretty format) a class' subclasses.

Usage:
    python3 psubclass.py <class_name>

Example:
    python3 psubclass.py Exception
"""

import argparse
import sys

def get_children(parent):
    """
    Returns a formatted list of the subclasses of the given parent class.

    Args:
        parent (class): The parent class.

    Returns:
        List[class]: The subclasses of the parent class.
    """
    try:
        return eval(parent).__subclasses__()
    except NameError:
        return []

def sort_class(class_name):
    return sorted(class_name, key=lambda x: x.__name__)

def subclasses(parent, indent=""):
    """
    Recursively finds all subclasses of the given parent class.

    Args:
        parent (class): The parent class.
    """
    children = get_children(parent)
    if children:
        for child in sort_class(children):
            name = child.__name__
            print(f'{indent}+ {name}')
            grandchildren = get_children(name)
            if grandchildren:
                subclasses(name, indent = indent + "|-- ")

def get_input():
    """
    Prompts the user for input if the script is being run in the REPL, or
    parses command-line arguments if the script is being run from the command line.

    Returns:
        str: The class name entered by the user.
    """

    input_help = 'Name of the class to find subclasses of: '
    
    if len(sys.argv) > 1:
        #parse CLI args
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description='Find subclasses of a given class: ')
        parser.add_argument('class_name', type=str, help=input_help)
        args = parser.parse_args()
        return args.class_name
    else:
        #prompt user
        return input(input_help)


def main():
    """
    Get input and runs the script.
    """

    class_name = get_input()

    # Find subclasses
    subclasses(class_name)

if __name__ == '__main__':
    main()

