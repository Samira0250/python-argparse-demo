#! /usr/bin/env python3

"A demonstration of using the argparse module to process command-line arguments."

import argparse

if __name__ == '__main__':
    # Create a command-line parser object
    parser = argparse.ArgumentParser(
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

    # Optional integer argument
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=1,
        help='An integer.',
    )

    # Optional floating-point argument
    parser.add_argument(
        '-t', '--threshold',
        type=float,
        default=3.4,
        help='A super duper important threshold.',
    )

    # Optional boolean argument
    parser.add_argument(
        '-c', '--i-am-cool',
        default=False,
        action='store_true',
        help='A boolean option.',
    )

    # ✨ New optional argument: your field of interest
    parser.add_argument(
        '--field',
        type=str,
        default='biomedical science',
        help='Your field of interest (e.g., neuroscience).'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Print all parsed arguments
    print(
        "The args after being processed by the argparse parser object:\n",
        args
    )

    # Access positional argument
    print("Paths:", args.file_path)

    # Access other keyword arguments
    print("Number:", args.number)
    print("Threshold:", args.threshold)
    print("I am cool?", args.i_am_cool)

    # Access your new field argument
    print(f"Running this search as a {args.field} Brain researcher")
