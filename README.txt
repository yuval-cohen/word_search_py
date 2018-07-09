Word Search:

A program in python that finds all words from a word list file (such as .\word.list) that can be found in a [n x m] grid of letters.

The grid should be given as a list of n m-letter strings, e.g. (n = m = 4):

grid = ["abcd", "edfg", hijk", "lmno"]

This represents the folling grid:
a b c d
e d f g
h i j k
l m n o

Details:
A word can be found in a grid by starting on any letter, then moving to an adjacent letter and so on.

Example 1:

a b a n
z q z d
r r o r
r n r r

The word "abandon" fits in the grid first horizontally, then diagonally down and to the left. The
word "ran" does NOT fit in the grid because 'r' and 'a' are not adjacent.

A word cannot use a specific letter in the grid more than once.

Example 2:

The grid
z z z z
z z b z
h z e z
a z z z

contains the words "be", "ha", and "ah". It should not contain "bee" or "ebb" or "he" or "hah".

Your program prints any word found to the standard output.

Your program assumes that the word list file contains no duplicated words and that all inputs are valid.

Your program is not tolerant to word files that contain a mixture of upper and lower case
words and of words that contain punctuation.

The program expects the grid as a parameter to WordSearch and print the results to the standard output. 
To run simply type:
python main.py

The output is a list of found words separated by newlines.

Comments:
(1) in word_search.py:
    You can choose to import WordList class from either WordListTree or from WordListSet:
    // by comment in/out one of the following import:
    from word_list import WordListTree as WordList
    #from word_list import WordListSet as WordList