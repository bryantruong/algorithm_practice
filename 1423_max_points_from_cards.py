class Solution:
    def maxScore(self, cardPoints, k) -> int:
        best_sum = None
        curr_start = len(cardPoints) - k
        # This will be used once we wrap around
        curr_stop = 0
        # Set start of k-size array to be k from the back
        curr_sum = sum(cardPoints[curr_start:])
        # Set the best_sum to this current sum, since we have none other
        best_sum = curr_sum
        # This will run until the current_start exceeds the length of cardPoints
        while True:
            curr_sum -= cardPoints[curr_start]
            curr_sum += cardPoints[curr_stop]
            if curr_sum > best_sum:
                best_sum = curr_sum
            # Move the pointers
            curr_start += 1
            if curr_start > len(cardPoints) - 1:
                break
            curr_stop += 1
        return best_sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Use a simple tree, with s and t matching, to test checkEquality
    test_case = [2,1000,1]
    test_k = 1
    solution_instance = Solution()
    print(solution_instance.maxScore(test_case, test_k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
