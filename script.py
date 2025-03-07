#!/usr/bin/env python3
import sys

def read_file(filename: str) -> list:
    """Open a file, return its contents as a list of lines.
    Return a message if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return ['file not found!\n']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: no file specified.")
    else:
        filename = sys.argv[1]
        content = read_file(filename)
        print("".join(content).strip())  # Print file contents without extra newlines
        print(f"Number of lines: {len(content)}")
