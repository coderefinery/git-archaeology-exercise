import sys

def load_text(filename):
    """
    Load lines from a plain-text file and return these as a list, with
    trailing newlines stripped.
    """
    with open(filename, "r") as input_fd:
        lines = input_fd.read().splitlines()
    return lines

if __name__ == '__main__':
    input_file = sys.argv[1]
    lines = load_text(input_file)
