'''
Given a screen.

Input: rows (int) and cols (int) and the list of strings (the sentence).
Output: the number of times the sentence can fit on the screen

You cannot put wrap words/strings onto multiple lines.

You cannot change the order of the words (since that would ruin the sentence meaning).

Each word must be separated by a single space, unless there is a new line. Delimiter can be " " or "\n"

How many times are we able to fit the sentence on the screen?

Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---


Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--
'''


def fit_on_screen(rows, cols, sentence):

    last_word_index = len(sentence) - 1  # 3
    row_i = 0
    col_i = 0
    num_placed = 0
    curr_word_i = 0
    while row_i < rows and col_i <= cols:
        curr_word_i = curr_word_i % len(sentence)
        curr_word = sentence[curr_word_i]
        # If adding the word fits with a space after it, we can stay on this row
        if col_i + len(curr_word) + 1 <= cols:
            col_i = col_i + len(curr_word) + 1
            if curr_word_i == last_word_index:
                num_placed += 1
            curr_word_i += 1
        # If adding the word just barely fits (no space after it), move down to the next row
        elif col_i + len(curr_word) == cols:
            col_i = 0
            row_i += 1
            if curr_word_i == last_word_index:
                num_placed += 1
            curr_word_i += 1
        else:
            col_i = 0
            row_i += 1
    return num_placed


if __name__ == '__main__':
    print(fit_on_screen(rows=2, cols=8, sentence=["hello", "world"]))
    print(fit_on_screen(rows=3, cols=6, sentence=["a", "bcd", "e"]))
    print(fit_on_screen(rows=4, cols=5, sentence=["I", "had", "apple", "pie"]))
