"""
    Search words from a 4x4 grid in a word-list input file.

"""
from word_search import WordSearch

grid1 = ["abig", "mica", "ahil", "yuva"]
grid2 = ["abom", "bani", "lene", "sess"]
grid3 = ["igai", "abvl", "yuka", "mich"]
word_search = WordSearch(grid1, "word.list")
word_search.print_found_words()
print(word_search.found_words(), "words found")
