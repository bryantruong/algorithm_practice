from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):

        """
        This is suboptimal. The best way would be to categorize by each letter's count.
        """
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word_iter = sorted(word)
            sorted_word_str = "".join(sorted_word_iter)
            # since this is a defaultdict, we can directly append without checking if in dict
            anagrams[sorted_word_str].append(word)

        # Produce output list
        output = []
        for anagram_group in anagrams.values():
            output.append(anagram_group)
        return output
