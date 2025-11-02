#!/usr/bin/env python3
"""
mapper.py - Hadoop MapReduce mapper script for extracting id, company, and totalyearlycompensation
from salaries.csv. Outputs: id<TAB>company,totalyearlycompensation
"""

import sys
import csv

def main():
    """
    Reads CSV input from stdin and prints id, company, and totalyearlycompensation
    in the format: id<TAB>company,totalyearlycompensation
    """
    reader = csv.DictReader(sys.stdin)
    for row in reader:
        try:
            _id = row.get("id", "").strip()
            company = row.get("company", "").strip()
            compensation = row.get("totalyearlycompensation", "").strip()
            if _id and company and compensation:
                print(f"{_id}\t{company},{compensation}")
        except Exception:
            continue  # Skip malformed rows

if __name__ == "__main__":
    main()
