#!/usr/bin/env python3
"""
This module provides a function to delete multiple directories from HDFS using the snakebite client.
"""

from snakebite.client import Client

def deletedir(l):
    """
    Deletes directories from HDFS based on a list of paths.

    Args:
        l (list): A list of strings, each representing a directory path to delete from HDFS.

    Returns:
        None
    """
    client = Client('localhost', 9000)
    for path in l:
        for result in client.delete([path], recurse=True):
            pass  # delete returns a generator; iterating triggers the operation
