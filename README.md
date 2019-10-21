# Word count example

These programs will count words in a given text, plot a bar chart of the 10
most common words, and test [Zipf's
law](https://en.wikipedia.org/wiki/Zipf%27s_law) on the two most common words.

- Simplified version of a [full word-count example project](https://github.com/coderefinery/word-count).
- Inspired by and derived from https://hpc-carpentry.github.io/hpc-python/
  which is distributed under
  [Creative Commons Attribution license (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/).


## Usage

Four texts are provided in the `data/` directory:
```shell
$ ls data/
LICENSE_TEXTS.md abyss.txt        isles.txt        last.txt         sierra.txt
```

To calculate the word frequency distribution of a given text file:
```shell
$ python source/wordcount.py data/abyss.txt output.dat
```

