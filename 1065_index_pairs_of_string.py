"""
Not a good solution. Use a prefix trie, but that is out of the scope of what I want to learn at the moment.
"""

class Solution:
    def indexPairs(self, text: str, words):
        solution_list = []
        for word in words:
            start = text.find(word)
            if start != -1:
                solution_list.append((start, start + len(word) - 1))
                # We have to continue to search the rest of the string for the same word
                while start != -1:
                    start = text.find(word, start + 1)
                    if start != -1:
                        solution_list.append((start, start + len(word) - 1))
        solution_list.sort()
        return solution_list