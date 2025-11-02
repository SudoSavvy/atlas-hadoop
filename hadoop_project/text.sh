#!/bin/bash
# text.sh - Displays the content of lao.txt from the /holbies/input directory on HDFS

# Show the content of lao.txt from HDFS
hdfs dfs -cat /holbies/input/lao.txt
