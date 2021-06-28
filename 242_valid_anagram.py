import bisect
from collections import defaultdict


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     sorted_s = sorted(s)
    #     sorted_t = sorted(t)
    #     return sorted_s == sorted_t

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic = defaultdict(lambda: 0)
        t_dic = defaultdict(lambda: 0)
        for letter in s:
            s_dic[letter] += 1
        for letter in t:
            t_dic[letter] += 1
        return s_dic == t_dic

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_s = "rac"
    test_t = "car"
    solution_instance = Solution()
    print(solution_instance.isAnagram(test_s, test_t))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
