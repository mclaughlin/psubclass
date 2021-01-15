#!/usr/bin/env python3

"""
Simple script to output a class' sub (or child) classes
"""

import argparse
import sys

__version__ = '0.0.1'

class Subclasses:

    def children(self, parent, children=None):
        """
        Returns list of subclasses given a parent class
        """

        if children is None:
            children = []
        try:
            children = [ 
                str(child)[8:-2:] 
                for child in eval(parent).__subclasses__()
            ]
        except (AttributeError, NameError) as e:
            pass
        return children

def main(parent):
    subclasses = Subclasses()
    children = subclasses.children(parent)
    for child in children:
        print('-'*40+f'\n+ {child}')
        sub_subclasses = Subclasses()
        grandchildren = sub_subclasses.children(child)
        for grandchild in grandchildren:
            print(f'  - {grandchild}')

if __name__ == '__main__':
    main(sys.argv[1:2][0])
