#! /usr/bin/env python

# Standard Lib Imports
import sys
# Third-Party Imports

# CUSTOM Imports
from app import run

value = sys.argv[1]

if __name__ == '__main__':
    run(value=value)
