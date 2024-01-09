#!/usr/bin/python3
class MyList(list):
    """Subclass of list with a method to print sorted elements."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
