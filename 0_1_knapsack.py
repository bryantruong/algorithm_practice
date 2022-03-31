import numpy as np
from random import seed
from random import randint

class Solution:
    def knapsack(self, values, weights, maxWeightConstraint):
        '''
        :type values: list of int
        :type weights: list of int
        :type maxWeightConstraint: int
        :rtype: int
        '''
        dp = [0 for _ in range(maxWeightConstraint + 1)]
        for curr_value, curr_weight in zip(values, weights):
            # Iterate backwards to prevent double counting
            for index_to_update in range(maxWeightConstraint, curr_weight - 1, -1):
                dp[index_to_update] = max(dp[index_to_update], curr_value + dp[index_to_update - curr_weight])
        return dp[maxWeightConstraint]


if __name__ == '__main__':
    solution = Solution()
    rng = np.random.default_rng(1)
    # values = rng.uniform(1, 100, 20) * 100
    # values = values.astype(int)
    # weights = rng.uniform(1, 100, 20) * 100
    # weights = weights.astype(int)
    weights = [10, 5, 2, 8, 15, 11, 4, 7, 1, 20]
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(values)
    print(weights)
    max_weight_pct = .6
    maxWeight = int(max_weight_pct * sum(weights))
    print(solution.knapsack(values, weights, maxWeight))