#!/usr/bin/env python3
"""
This module provides a function to download files from HDFS
and store them in the user's /tmp directory.
"""

import os
from snakebite.client import Client

def download(l):
    """
    Downloads files from HDFS and stores them in the /tmp directory.

    Args:
        l (list): A list of strings, each representing a file path in HDFS.

    Returns:
        None
    """
    client = Client('localhost', 9000)
    for hdfs_path in l:
        local_path = os.path.join("/tmp", os.path.basename(hdfs_path))
        for result in client.copyToLocal([hdfs_path], local_path):
            pass  # copyToLocal returns a generator; iterating triggers the operation
