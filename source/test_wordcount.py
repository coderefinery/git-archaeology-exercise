import wordcount

def test_wordcount():
    lines = wordcount.load_text('data/isles.txt')
    counts = wordcount.calculate_word_counts(lines)
    sorted_counts = wordcount.word_count_dict_to_tuples(counts)
    sorted_counts = wordcount.filter_word_counts(sorted_counts)
    correct = [('the', 3822), ('of', 2460), ('and', 1723), ('to', 1479)]
    assert sorted_counts[0:4] == correct

