import bisect


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

    # My somewhat lengthy solution. Bisect module is a cheat code
    """
    class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def get_next_greatest(left, right):
            # Base cases
            if left == right:
                if letters[right] > target:
                    return letters[right]
                while right < len(letters):
                    if letters[right] <= target:
                        right += 1
                    else:
                        return letters[right]
                return letters[0]
            # We can now assume that there are at least three letters under consideration
            midpoint = (left + right) // 2
            if letters[midpoint] == target:
                while midpoint < len(letters):
                    if letters[midpoint] == target:
                        midpoint += 1
                    else:
                        return letters[midpoint]
                return letters[0]
            elif letters[midpoint] < target: # the midpoint is smaller than what we are looking for, so look right
                return get_next_greatest(midpoint + 1, right)
            else:
                return get_next_greatest(left, midpoint)
        
        return get_next_greatest(left=0, right=len(letters)-1)
    
    """


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_case = (["c","f","j"], "a")
    solution_instance = Solution()
    print(solution_instance.nextGreatestLetter(test_case[0], test_case[1]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
