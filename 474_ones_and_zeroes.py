def get_counts(string_number):
    zero_count, ones_count = 0, 0
    for char in string_number:
        if int(char) == 0:
            zero_count += 1
        else:
            ones_count += 1
    return zero_count, ones_count


class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        # Memoization dictionary.
        memo_dict = {}

        def try_subset(curr_index, zeros_left, ones_left):
            # The base case, when we have no option to add anything.
            if curr_index >= len(strs):
                return 0
            if (curr_index, zeros_left, ones_left) in memo_dict:
                return memo_dict[(curr_index, zeros_left, ones_left)]
            else:
                curr_str = strs[curr_index]
                zeros, ones = get_counts(curr_str)
                adding_result = float("-inf")
                # Try adding this current string to the subset
                if zeros <= zeros_left and ones <= ones_left:
                    # Since we are adding the element, add one as we unwind.
                    adding_result = try_subset(curr_index + 1, zeros_left - zeros, ones_left - ones) + 1
                skip_result = try_subset(curr_index + 1, zeros_left, ones_left)
                memo_dict[(curr_index, zeros_left, ones_left)] = max(skip_result, adding_result)
                return memo_dict[(curr_index, zeros_left, ones_left)]

        return try_subset(0, m, n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_strs = ["10","0001","111001","1","0"]
    test_m = 5
    test_n = 3
    solution_instance = Solution()
    print(solution_instance.findMaxForm(test_strs, test_m, test_n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
