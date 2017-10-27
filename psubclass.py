#!/usr/bin/env python

"""Simple script to output a classes sub (or child) classes"""

import argparse
import sys

__version__ = '0.0.1'

class Subclasses:
    """
    Class to output a list of a classes subclasses
    """

    def children(self, parent, children=None):
        if children is None:
            children = []
        try:

            children = str(child)[8:-2:] \
                       for child in eval(parent).__subclasses__():

            #above list comprehension same as:
            #for child in eval(parent).__subclasses__():
                #child = str(child)[8:-2:]
                #children.append(child)

        except (AttributeError, NameError) as e:
            pass
        return children

def main(parent):
    subclasses = Subclasses()
    children = subclasses.children(parent)
    for child in children:
        print('-'*40)
        print(f'+ {child}')
        sub_subclasses = Subclasses()
        grandchildren = sub_subclasses.children(child)
        for grandchild in grandchildren:
            print(f'  - {grandchild}')

if __name__ == '__main__':
    main(sys.argv[1:2][0])
