#!/bin/bash
# lao.sh - Uploads the file lao.txt to the /holbies/input directory on HDFS

# Upload lao.txt to HDFS
hdfs dfs -put lao.txt /holbies/input/
