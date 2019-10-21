import sys

def load_text(filename):
    """
    Load lines from a plain-text file and return these as a list, with
    trailing newlines stripped.
    """
    with open(filename, "r") as input_fd:
        lines = input_fd.read().splitlines()
    return lines

def update_word_counts(line, counts):
    words = line.split()
    for word in words:
        word = word.lower().strip()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

def calculate_word_counts(lines):
    counts = {}
    for line in lines:
        update_word_counts(line, counts)
    return counts

def word_count(input_file):
    lines = load_text(input_file)
    counts = calculate_word_counts(lines)
    return counts


if __name__ == '__main__':
    input_file = sys.argv[1]
    counts = word_count(input_file)
    print(counts)
