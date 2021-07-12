class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pairings = {'0': '0',
                    '1': '1',
                    '6': '9',
                    '8': '8',
                    '9': '6'}
        left = 0
        right = len(num) - 1
        while left <= right:
            if num[left] not in pairings or num[right] not in pairings:
                return False
            # Check that the right value matches the left's pairing
            if pairings[num[left]] != num[right]:
                return False
            # Else, move both in
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    test_nums = "88"
    solution_instance = Solution()
    print(solution_instance.isStrobogrammatic(test_nums))