#!/bin/bash
# createdirectories.sh - Creates /holbies and /holbies/input directories in HDFS

# Create the /holbies directory
hdfs dfs -mkdir -p /holbies

# Create the /holbies/input directory
hdfs dfs -mkdir -p /holbies/input
