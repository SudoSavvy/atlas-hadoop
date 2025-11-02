#!/usr/bin/env python3
"""
This module provides a function to create multiple directories in HDFS using the snakebite client.
"""

from snakebite.client import Client

def createdir(l):
    """
    Creates directories in HDFS from a list of paths.

    Args:
        l (list): A list of strings, each representing a directory path to create in HDFS.

    Returns:
        None
    """
    client = Client('localhost', 9000)
    for path in l:
        for result in client.mkdir([path], create_parent=True):
            pass  # mkdir returns a generator; iterating triggers the operation
