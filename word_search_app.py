import sys
from word_search import WordSearch

def main(word_list_filename, grid):
    word_search = WordSearch(grid, word_list_filename)
    word_search.print_found_words()
    print(word_search.found_words(), "words found")


if __name__ == "__main__":
    file_name = sys.argv[1]
    grid = sys.argv[2:]
    main(file_name, grid)


from word_list import WordListSet, FindWord

def test_finding_all_words():
    grid = ["abom", "bani", "lene", "sess"]
    word_search = WordSearch(grid, "word.list")
    word_list = WordListSet("word.list")
    for word in word_list.word_list:
        if word_search._word_list.find_word(word) != FindWord.WORD_FOUND:
            print(word)
