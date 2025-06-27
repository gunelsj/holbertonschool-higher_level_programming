#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""

class MyList(list):
    """
    MyList class that extends the built-in list class
    with a method to print the list sorted.
    """
    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
