import argparse
import re

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

# Optional argument: your field of interest
parser.add_argument(
    '--field',
    type=str,
    default='biomedical science',
    help='Your field of interest (e.g., neuroscience).'
)

# Parse arguments
args = parser.parse_args()

# Print field info
print(f"Running this search as a {args.field} brain researcher ")

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
