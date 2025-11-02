#!/usr/bin/env python3
"""
reducer.py - Hadoop MapReduce reducer script to extract the top 10 salaries
based on totalyearlycompensation from mapper output.
"""

import sys

def main():
    """
    Reads mapper output from stdin, extracts salary data, and prints the top 10
    entries sorted by totalyearlycompensation in descending order.
    """
    top_salaries = []

    for line in sys.stdin:
        try:
            line = line.strip()
            if not line:
                continue
            # Expected format: id<TAB>company,totalyearlycompensation
            parts = line.split('\t')
            if len(parts) != 2:
                continue
            _id = parts[0]
            company_comp = parts[1].split(',')
            if len(company_comp) != 2:
                continue
            company = company_comp[0]
            compensation = int(company_comp[1])

            # Store as tuple: (compensation, id, company)
            entry = (compensation, _id, company)

            if len(top_salaries) < 10:
                top_salaries.append(entry)
            else:
                # Replace lowest if current is higher
                top_salaries.sort()
                if compensation > top_salaries[0][0]:
                    top_salaries[0] = entry
        except Exception:
            continue  # Skip malformed lines

    # Sort final top 10 in descending order
    top_salaries.sort(reverse=True)

    for comp, _id, company in top_salaries:
        print(f"{_id}\t{company},{comp}")

if __name__ == "__main__":
    main()
