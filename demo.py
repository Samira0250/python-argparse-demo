#!/usr/bin/env python3
"""
A word search demo using argparse.
This script reads one or more text files, searches for words containing a specified pattern,
prints matches for each file, and saves all matches to 'matches.txt'.
"""

import argparse
import re

if __name__ == '__main__':
    # Create parser
    parser = argparse.ArgumentParser(
        description="Search for words containing a pattern in one or more text files.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Positional argument: one or more file paths
    parser.add_argument(
        'file_path',
        type=str,
        metavar='FILE-PATH',
        nargs='+',
        help='Path(s) to text file(s) to search.',
    )

    # Optional argument: word/pattern to search for
    parser.add_argument(
        '-w', '--word',
        type=str,
        default='herit',
        help='Word or pattern to search for in files.',
    )

    # Parse arguments
    args = parser.parse_args()

    # Compile regex pattern for the search word (case-insensitive)
    pattern = re.compile(rf'\w*{args.word}\w*', re.IGNORECASE)

    all_matches = []

    # Process each file
    for file in args.file_path:
        try:
            with open(file, 'r') as f:
                text = f.read()
            matches = pattern.findall(text)
            print(f"Matches in {file}: {matches}")
            all_matches.extend(matches)
        except FileNotFoundError:
            print(f"File '{file}' not found!")

    # Save all matches to a file
    with open("matches.txt", "w") as f:
        f.write("\n".join(all_matches))
