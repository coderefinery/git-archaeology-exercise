import wordcount

def test_calculate_word_counts():
    """ Test for function wordcounts.calculate_word_counts() """

    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit \n sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\n nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\n reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla\n pariatur. Excepteur sint occaecat cupidatat non proident, sunt in\n culpa qui officia deserunt mollit anim id est laborum'

    lines = text.splitlines()

    correct_counts = {'lorem': 1, 'ipsum': 1, 'dolor': 2, 'sit': 1, 'amet': 1, 'consectetur': 1, 'adipiscing': 1, 'elit': 1, 'sed': 1, 'do': 1, 'eiusmod': 1, 'tempor': 1, 'incididunt': 1, 'ut': 3, 'labore': 1, 'et': 1, 'dolore': 2, 'magna': 1, 'aliqua': 1, 'enim': 1, 'ad': 1, 'minim': 1, 'veniam': 1, 'quis': 1, 'nostrud': 1, 'exercitation': 1, 'ullamco': 1, 'laboris': 1, 'nisi': 1, 'aliquip': 1, 'ex': 1, 'ea': 1, 'commodo': 1, 'consequat': 1, 'duis': 1, 'aute': 1, 'irure': 1, 'in': 3, 'reprehenderit': 1, 'voluptate': 1, 'velit': 1, 'esse': 1, 'cillum': 1, 'eu': 1, 'fugiat': 1, 'nulla': 1, 'pariatur': 1, 'excepteur': 1, 'sint': 1, 'occaecat': 1, 'cupidatat': 1, 'non': 1, 'proident': 1, 'sunt': 1, 'culpa': 1, 'qui': 1, 'officia': 1, 'deserunt': 1, 'mollit': 1, 'anim': 1, 'id': 1, 'est': 1, 'laborum': 1}

    counts = wordcount.calculate_word_counts(lines)

    assert counts == correct_counts
