import heapq


class Solution:
    """
    Given an integer array of stones
    Each turn, choose the heaviest two stones and smash them together
    If the two are equal, both are destroyed
    If not, subtract the weight of the smaller stone from the bigger stone. The bigger stone remains.
    At the end of the game there is at most one stone left.



    Ex: [8, 7, 4, 2, 1, 1]
    Smash together 8 and 7. [4, 2, 1, 1, 1]
    Smash together 4 and 2. [2, 2, 1, 1, 1]
    Smash together 2 and 2. [1, 1, 1]
    Smash together 1 and 1. [1]
    Return 1

    Time complexity if you do not use a min heap: O(N) to get the two heaviest each time (N times): O(N^2)
    Time complexity if you do use a min heap: O(Nlogn) to do initial heapsort, log N to each insert: O(nlogn)
    """

    def lastStoneWeight(self, stones) -> int:
        # Have to invert everything because heapq only implements a minheap (as opposed to a maxheap)
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            diff = y - x
            if diff != 0:
                heapq.heappush(stones, diff)
        if stones:
            # Invert back to normal weight
            return -1 * heapq.heappop(stones)
        return 0


if __name__ == '__main__':
    test_stones = [2, 7, 4, 1, 8, 1]
    solution_instance = Solution()
    print(solution_instance.lastStoneWeight(test_stones))
