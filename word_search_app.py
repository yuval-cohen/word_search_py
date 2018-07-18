#!/usr/bin/env python3
"""A program searches and print all words that can be constructed
from a grid of letters in an input word-list UTF-8 text file.
By default, the programs prints the words to the standard output.

The grid should be n m-letter strings, e.g. (n = m = 4):
a b c d
e d f g
h i j k
l m n o

A word can be constructed from a grid by starting on any letter,
then moving to an adjacent letter and so on. E.g.:

a b a n
z q z d
r r o r
r n r r

The word "abandon" fits in the grid first horizontally, then diagonally
down and to the left. The word "ran" does NOT fit in the grid because
'r' and 'a' are not adjacent.

The input word-list UTF-8 text file is a file contains list of words
each word in a single line.

Example:
    input file: .\word.list
    grid:
        m a n
        y o u
        a r e
        b a d
    python word_search_app.py "word.list" man you are bad

Attributes:
    none
"""

import sys

from word_list import WordListSet
from word_list import WordListTree
from word_list import FindWord
from word_search import WordSearch

def main(word_list_filename, grid):
    """The main function of word_search_app program.

        Args:
            word_list_filename (str) - full path input word-list text file
            grid (list) - letters grid as list of n m-letters str

        Returns:
            none
    """
    word_search = WordSearch(grid, word_list_filename)
    word_search.print_found_words()
    print(word_search.found_words(), "words found")


if __name__ == "__main__":
    file_name = sys.argv[1]
    grid = sys.argv[2:]
    main(file_name, grid)


def test_finding_all_words(word_list_filename):
    """Test function that tests if all words in word-list file
    using WordListSet are found through WordListTree.

        Args:
            word_list_filename (str) - full path input word-list text file

        Returns:
            True - if all words are found
            False - otherwise
    """
    word_list_set = WordListSet("word.list")
    word_list_tree = WordListTree("word.list")
    result = True
    for word in word_list_set._word_list:
        if word_list_tree.find_word(word) != FindWord.WORD_FOUND:
            result = False
            print("word '" + word + "' - NOT FOUND!")  # print not found word

    if result:
        print("test_finding_all_words [OK]")
    else:
        print("test_finding_all_words [FAIL]")
