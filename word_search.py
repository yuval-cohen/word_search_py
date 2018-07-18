"""This module contains WordSearch class for searching for all words
that can be constructed from a grid of letters in an input word-list
UTF-8 text file. Found words are printed (default = standard output).

The grid should be given as a list of n m-letter strings, e.g. (n = m = 4):

grid = ["abcd", "edfg", hijk", "lmno"]

This represents the following grid:
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
    grid = ["abc", "efg", "gov", "zbz"]
    word_search = WordSearch(grid, "word.list")
    word_search.print_found_words()

Attributes:
    none.
"""

from word_list import WordListTree as WordList
from word_list import FindWord

class WordSearch:
    """A class for searching for all words that can be constructed from
    a grid of letters from an input word-list UTF-8 text file.

    Attributes:
        _word_list (WordList) - contains all words from the input
            word-list text file
        _print_func (default = print) - print word function
        _no_found_words (int) - number of found words
        _grid (list) - letters grid as list of n m-letters str
        _grid_rows (int) - number of rows in grid
        _grid_columns (int) - number of columns in grid
    """

    def __init__(self, grid, word_list_filename, print_func=print):
        """Inits WordSearch from an grid of letters and from
        input word-list text file.

        Args:
            grid (list) - letters grid as list of n m-letters str
            word_list_filename (str) - full path input word-list text file.
            print_func (func(x)) - [optional] print word function
        """
        self.set_grid(grid)
        self._word_list = WordList(word_list_filename)
        self._print_func = print_func
        self._no_found_words = 0


    def set_grid(self, grid):
        """Sets (new) grid of letters in WordSearch object.

        Args:
            grid (list) - letters grid as list of n m-letters str

        Returns:
            none
        """
        self._grid = list(grid)
        self._grid_rows = len(grid)
        self._grid_columns = len(grid[0])


    def set_print_func(self, print_func):
        """Sets print function to print all found words.

        Args:
            print_func (func(x)) - print word function

        Returns:
            none
        """
        self._print_func = print_func


    def print_found_words(self):
        """Find all words from a grid in WordSearch object
        and print them.

        Args:
            none

        Returns:
            none
        """
        self._no_found_words = 0
        for i in range(self._grid_rows):
            for j in range(self._grid_columns):
                grid_ctrl = list()
                for row in range(self._grid_rows):
                    grid_ctrl.append(list([False] * self._grid_columns))

                grid_ctrl[i][j] = True
                word = self._grid[i][j]
                self._print_found_words_from_prefix(word, i, j, grid_ctrl)


    def found_words(self):
        """Returns number of found words in WordSearch object (after calling
        print_found_words).

        Args:
            none

        Returns:
            (int) no of found words.
        """
        return self._no_found_words


    def _print_found_words_from_prefix(self, word, i, j, grid_ctrl):
        word_found = self._word_list.find_word(word)
        if word_found == FindWord.WORD_FOUND or word_found == FindWord.PREFIX_FOUND:
            if word_found == FindWord.WORD_FOUND:
                self._print_func(word)
                self._no_found_words += 1

            for x, y in self._next_adj_unused_cell(grid_ctrl, i, j):
                # prepare next word
                word_next = word + self._grid[x][y]

                # prepare next word_search ctrl
                grid_ctrl_next = []
                for l in grid_ctrl:
                    grid_ctrl_next.append(list(l))
                grid_ctrl_next[x][y] = True

                self._print_found_words_from_prefix(word_next, x, y, grid_ctrl_next)


    def _next_adj_unused_cell(self, grid_ctrl, i, j):
        x, y = i, j

        x = i - 1
        if x >= 0 and x < self._grid_rows and \
            y >= 0 and y < self._grid_columns and \
            grid_ctrl[x][y] == False:
            yield x, y

        y = j + 1
        if x >= 0 and x < self._grid_rows and \
            y >= 0 and y < self._grid_columns and \
            grid_ctrl[x][y] == False:
            yield x, y

        x = i
        if x >= 0 and x < self._grid_rows and \
            y >= 0 and y < self._grid_columns and \
            grid_ctrl[x][y] == False:
            yield x, y

        x = i + 1
        if x >= 0 and x < self._grid_rows and \
            y >= 0 and y < self._grid_columns and \
            grid_ctrl[x][y] == False:
            yield x, y

        y = j
        if x >= 0 and x < self._grid_rows and \
            y >= 0 and y < self._grid_columns and \
            grid_ctrl[x][y] == False:
            yield x, y

        y = j - 1
        if x >= 0 and x < self._grid_rows and \
            y >= 0 and y < self._grid_columns and \
            grid_ctrl[x][y] == False:
            yield x, y

        x = i
        if x >= 0 and x < self._grid_rows and \
            y >= 0 and y < self._grid_columns and \
            grid_ctrl[x][y] == False:
            yield x, y

        x = i - 1
        if x >= 0 and x < self._grid_rows and \
            y >= 0 and y < self._grid_columns and \
            grid_ctrl[x][y] == False:
            yield x, y

        return
