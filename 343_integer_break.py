class Solution:
    def integerBreak(self, n: int) -> int:
        memo_table = [None for _ in range(n + 1)]
        memo_table[0] = 0
        memo_table[1] = 0

        def get_product(num):
            """
            Helper recursive function to get the best possible product.
            The recursive relation is to try to subtract 1 to num - 1 from num and multiply by the max of that value or
            its recursive solution (the maximum product for that complement). Will be very time inefficient until
            we memoize it.
            :param num: The target number for which we are trying to get the maximum product
            :return: The maximum product you can get
            """
            # Base Case:
            if memo_table[num]:
                return memo_table[num]
            if num == 1:
                return 0
            max_product = float('-inf')
            # We need to try out each permutation of numbers that sum to n
            for subtract_amount in range(1, num):
                complement = num - subtract_amount
                curr_product = subtract_amount * max(complement, get_product(complement))
                max_product = max(max_product, curr_product)
            memo_table[num] = max_product
            return max_product

        return get_product(n)


if __name__ == '__main__':
    n = 10
    solution_instance = Solution()
    solution_to_return = solution_instance.integerBreak(n)
    print(solution_to_return)
