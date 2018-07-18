"""This module contains two class of WordList:
(1) WordListSet and (2) WordListTree
although implemented differently, they provide the same functionality.
Both WordList classes provide interface to find a word from an
input word-list UTF-8 text file.
The input word-list UTF-8 text file is a file contains list of words
each word in a single line.

Example:
    word.list file:
    I
    go
    to
    school
    every
    day
    ...
    from word_list import WordListSet (or WordListTree) as WordList
    word_list = WordList("word.list")
    if (word_list.find_word("school") == FindWord.WORD_FOUND)
        print ("The word 'school' is found in word.list")

Attributes:
    none.

"""

from enum import Enum

class FindWord(Enum):
    """Enum class for the return value of WordListXXX.find_word."""
    WORD_FOUND = 1
    PREFIX_FOUND = 2
    NOT_FOUND = 3


class WordListSet:
    """A class for finding a word in an input word-list UTF-8 text file.

    Attributes:
        _word_list (set) - a set that contains all words from the input
            word-list text file.
    """

    def __init__(self, filename):
        """Inits WordListSet from an input word-list text file.

        Args:
            filename (str) - full path input word-list text file.
        """
        with open(filename, mode="rt", encoding="utf-8") as in_file:
            self._word_list = set()
            for word in in_file:
                self._word_list.add(word.rstrip())  # strip the newline at the end


    def find_word(self, word):
        """Finds a word from word list.

        Args:
            word (str): word to be found.

        Returns:
            FindWord.WORD_FOUND if word found,
            FindWord.PREFIX_FOUND otherwise.
        """
        if word in self._word_list:
            return FindWord.WORD_FOUND
        return FindWord.PREFIX_FOUND


    def no_of_words(self):
        """Returns no of words in word-list.

        Args:
            none.

        Returns:
            (int) no of words.
        """
        return len(self._word_list)


class _CharNode:

    def __init__(self, ch, is_word=False, adjacent=None, next=None):
        self.ch = ch
        self.is_word = is_word
        self.adjacent = adjacent
        self.next = next


class WordListTree:
    """A class for finding a word in an input word-list UTF-8 text file.

    Attributes:
        _char_tree (_CharNode) - tree of characters that contains all words.
        _no_of_words (int) - no. of words in word-list
        _no_of_char_nodes (int) - no of character nodes in _char_tree
                                  (for statistics).
    """

    def __init__(self, filename):
        """Inits WordListTree from an input word-list text file.

        Args:
            filename (str) - full path input word-list text file.
        """
        self._char_tree = None
        self._no_of_words = 0
        self._no_of_char_nodes = 0
        with open(filename, mode="rt", encoding="utf-8") as in_file:
            for word in in_file:
                self._add_word_to_tree(word.rstrip())
                self._no_of_words += 1


    def _add_word_to_tree(self, word):
        nxt_search = self._char_tree
        nxt_search_prev = None
        for i in range(len(word)):
            is_word = (i == (len(word) - 1))

            # no characters exist in this depth
            if nxt_search == None:
                char_node = _CharNode(word[i], is_word)
                self._no_of_char_nodes += 1
                nxt_search = char_node

                # initialise char tree if the very first character
                if self._char_tree == None:
                    self._char_tree = char_node
                else:
                    nxt_search_prev.next = nxt_search

                nxt_search_prev = nxt_search
                nxt_search = nxt_search.next

            # characters do exist in this depth
            else:
                char_added_to_adjacent = False

                # search ADJACENT list to find the correct spot to add
                # character to tree (if character does not exist)
                # ADJACENT list is kept sorted by character value
                adj_search = nxt_search
                while not char_added_to_adjacent:
                    adj_adj_search = adj_search.adjacent

                    if adj_search.ch == word[i]:
                        nxt_search_prev = adj_search
                        nxt_search = nxt_search_prev.next
                        char_added_to_adjacent = True  # character already exists - do nothing

                    elif adj_search.ch < word[i]:
                        if adj_adj_search == None:
                            # add character to the end of ADJACENT list
                            char_node = _CharNode(word[i], is_word)
                            self._no_of_char_nodes += 1

                            adj_search.adjacent = char_node
                            nxt_search_prev = char_node
                            nxt_search = nxt_search_prev.next
                            char_added_to_adjacent = True

                        elif adj_adj_search.ch > word[i]:
                            # add character between adj_search and adj_adj_search
                            char_node = _CharNode(word[i], is_word)
                            self._no_of_char_nodes += 1

                            adj_search.adjacent = char_node
                            char_node.adjacent = adj_adj_search

                            nxt_search_prev = char_node
                            nxt_search = nxt_search_prev.next
                            char_added_to_adjacent = True

                        # else adj_adj_search.ch <= word[i] - to be handled in the next iteration loop

                    else: # adj_search.ch > word[i]
                        # add character at the start of ADJACENT list
                        char_node = _CharNode(word[i], is_word)
                        self._no_of_char_nodes += 1

                        nxt_search_prev.next = char_node
                        char_node.adjacent = nxt_search

                        nxt_search_prev = char_node
                        nxt_search = nxt_search_prev.next
                        char_added_to_adjacent = True

                    adj_search = adj_search.adjacent


    def find_word(self, word):
        """Finds a word from word list.

        Args:
            word (str): word to be found.

        Returns:
            FindWord.WORD_FOUND - word found
            FindWord.PREFIX_FOUND - word is found as a prefix
                of another word
            FindWord.NOT_FOUND - otherwise (word not found)
        """
        word_len = len(word)
        search = self._char_tree
        while search != None:
            if search.ch == word[0]:
                if word_len == 1:
                    if search.is_word:
                        return FindWord.WORD_FOUND
                    else:
                        return FindWord.PREFIX_FOUND
                else:
                    return self._find_word(search.next, word[1:])
            elif search.ch > word[0]:
                return FindWord.NOT_FOUND
            # else - search.ch < word[0] - continue
            search = search.adjacent
        return FindWord.NOT_FOUND

    def _find_word(self, search_tree, word):
        word_len = len(word)
        search = search_tree
        while search != None:
            if search.ch == word[0]:
                if word_len == 1:
                    if search.is_word:
                        return FindWord.WORD_FOUND
                    else:
                        return FindWord.PREFIX_FOUND
                else:
                    return self._find_word(search.next, word[1:])
            elif search.ch > word[0]:
                return FindWord.NOT_FOUND

            # else - search.ch < word[0] - continue
            search = search.adjacent
        return FindWord.NOT_FOUND

    def no_of_words(self):
        """Returns no of words in word-list.

        Args:
            none.

        Returns:
            (int) no of words.
        """
        return self._no_of_words
