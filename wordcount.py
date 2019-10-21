import sys

DELIMITERS = ". , ; : ? $ @ ^ < > # % ` ! * - = ( ) [ ] { } / \" '".split()


def load_text(filename):
    """
    Load lines from a plain-text file and return these as a list, with
    trailing newlines stripped.
    """
    with open(filename, "r") as input_fd:
        lines = input_fd.read().splitlines()
    return lines

def update_word_counts(line, counts):
    for purge in DELIMITERS:
        line = line.replace(purge, " ")
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

def word_count_dict_to_tuples(counts, decrease=True):
    return sorted(list(counts.items()), key=lambda key_value: key_value[1],
                  reverse=decrease)

def filter_word_counts(counts, min_length=1):
    """
    Given a list of (word, count) tuples, create a new list with only
    those tuples whose word is >= min_length.
    """
    stripped = []
    for (word, count) in counts:
        if len(word) >= min_length:
            stripped.append((word, count))
    return stripped


def word_count(input_file, output_file, min_length=1):
    lines = load_text(input_file)
    counts = calculate_word_counts(lines)
    sorted_counts = word_count_dict_to_tuples(counts)
    sorted_counts = filter_word_counts(sorted_counts, min_length)
    with open(output_file, 'w') as output:
        for count in sorted_counts:
            output.write("%s\n" % " ".join(str(c) for c in count))



if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    min_length = 1
    if len(sys.argv) > 3:
        min_length = int(sys.argv[3])
    word_count(input_file, output_file, min_length)
