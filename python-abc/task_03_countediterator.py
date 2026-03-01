#!/usr/bin/python3
"""
This module defines a CountedIterator class.
It keeps track of how many items have been iterated over.
"""


class CountedIterator:
    """
    An iterator wrapper that maintains a counter of iterated items.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and the counter.

        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current number of items that have been iterated.
        """
        return self.count

    def __next__(self):
        """
        Increments the counter and fetches the next item.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self
