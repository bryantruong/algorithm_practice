from collections import defaultdict
from collections import deque

"""
Thought it might be a DP problem, but was just a graph problem.
Time Complexity: 
Complexity: O(N^2 * A^N + D)
where, N is Number of dials (4 in our case)
A is number of alphabets (10 in our case -> 0 to 9)
D is the size of deadends.

There are 10 x 10 x 10 x 10 possible combinations => 10^4 => A^N
For each combination, we are looping 4 times (which is N) and in each iteration, we assemble the substring, which is O(N).
    Therefore O(N^2) for each combination
Total complexity => A^N * N^2, plus D to create the hashset => N^2 * A^N + D
"""


class Solution:
    def openLock(self, deadends, target: str) -> int:
        dead_set = set(deadends)

        def get_neighbors(string_combo):
            # This is the solution list to append to
            possible_neighbors = []
            # We need to repeat the process for each digit:
            for digit_i in range(4):
                int_digit = int(string_combo[digit_i])
                for delta in [-1, 1]:
                    # We have to try to add one as well as subtracting one to each digit
                    # Use modulus to bound between 0 and 9
                    new_digit = (int_digit + delta) % 10
                    possible_neighbors.append(string_combo[:digit_i] + str(new_digit) + string_combo[digit_i + 1:])
            return possible_neighbors

        # Implement a standard BFS. Instead of adding children, add neighbors. Add checks for dead_set
        expanded = set()
        to_expand = deque()
        # We always start at 0000
        to_expand.append("0000")
        move_count = -1
        while to_expand:
            size = len(to_expand)
            move_count += 1
            for _ in range(size):
                curr_combo = to_expand.popleft()
                if curr_combo == target:
                    return move_count
                if curr_combo in expanded or curr_combo in dead_set:
                    continue
                # Otherwise, mark it as expanded
                expanded.add(curr_combo)
                # Add neighbors to be expanded
                to_expand.extend(get_neighbors(curr_combo))
        # If the target is not reachable
        return -1


if __name__ == '__main__':
    test_deadends = ["0201", "0101", "0102", "1212", "2002"]
    test_target = "0202"
    solution_instance = Solution()
    print(solution_instance.openLock(test_deadends, test_target))
