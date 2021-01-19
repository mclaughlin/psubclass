#!/usr/bin/env python3

"""
Simple script to output a class' sub (or child) classes
"""

import argparse, sys

def get_children(parent):
    try:
        children = eval(parent).__subclasses__()
        if children:
            return children
    except NameError:
        parent = None

def subclasses(parent):
    children = get_children(parent)
    if children:
        for child in children:
            name = child.__name__
            print(f'Child is {name}')
            grandchildren = get_children(name)
            print(grandchildren)
            if grandchildren:
                print(f'Grandchild is {name}')
                #subclasses(name)

def main(parent):
    subclasses(parent)

if __name__ == '__main__':
    main(sys.argv[1:2][0])

