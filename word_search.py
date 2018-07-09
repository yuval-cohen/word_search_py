
# can either import WordListTree or WordListSet as WordList
from word_list import WordListTree as WordList
#from word_list import WordListSet as WordList


class WordSearch:

    def __init__(self, grid, word_list_filename, print_func=print):
        self.set_grid(grid)
        self._word_list = WordList(word_list_filename)
        self._print_func = print_func
        self._found_words = 0


    def set_grid(self, grid):
        self._grid = list(grid)
        self._grid_rows = len(grid)
        self._grid_columns = len(grid[0])


    def set_print_func(self, print_func):
        self._print_func = print_func


    def print_found_words(self):
        self._found_words = 0
        for i in range(self._grid_rows):
            for j in range(self._grid_columns):
                grid_ctrl = list()
                for row in range(self._grid_rows):
                    grid_ctrl.append(list([False] * self._grid_columns))

                grid_ctrl[i][j] = True
                word = self._grid[i][j]
                self._print_found_words_from_prefix(word, i, j, grid_ctrl)


    def found_words(self):
        return self._found_words


    def _print_found_words_from_prefix(self, word, i, j, grid_ctrl):
        word_found = self._word_list.find_word(word)
        if word_found == "WORD_FOUND" or word_found == "PREFIX_FOUND":
            if word_found == "WORD_FOUND":
                self._print_func(word)
                self._found_words += 1

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
