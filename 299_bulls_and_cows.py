from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        char_to_index = defaultdict(lambda: [set(), 0])
        no_bulls, no_cows = 0, 0
        # populate the dictionary with each character and corresponding indices
        for index, char in enumerate(secret):
            char_to_index[char][0].add(index)
        for index, char in enumerate(guess):
            if char in char_to_index:
                if index in char_to_index[char][0]:
                    if len(char_to_index[char][0]) <= char_to_index[char][1]:
                        no_bulls += 1
                        no_cows -= 1
                    else:
                        no_bulls += 1
                else:
                    if len(char_to_index[char][0]) > char_to_index[char][1]:
                        no_cows += 1

                # Mark it as visited
                char_to_index[char][1] += 1
        return str(no_bulls) + "A" + str(no_cows) + "B"


if __name__ == '__main__':
    test_secret = "1123"
    test_guess = "0111"
    solution_instance = Solution()
    print(solution_instance.getHint(test_secret, test_guess))
