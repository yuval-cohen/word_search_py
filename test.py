"""
    Test to find all words in word.list as WordListSet using WordSearch that is using WordListTree
"""

def test_finding_all_words():
    from word_search import WordSearch
    from word_list import WordListSet

    grid = ["abom", "bani", "lene", "sess"]
    word_search = WordSearch(grid, "word_x.list")
    word_list = WordListSet("word_x.list")
    for word in word_list.word_list:
        if word_search._word_list.find_word(word) != "WORD_FOUND":
            print(word)


test_finding_all_words()
