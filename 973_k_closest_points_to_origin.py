import heapq


class Solution:
    """
    Return the k closest points to the origin (0,0). The available points are in the input array.
    Distance between points is the standard euclidian distance.

    points = [[1,3],[-2,2]], k = 1

    Algorithm:
    Initialize a priority queue.
    Looping through the points array.
        - Calculate the distance from origin. Add that as a tuple to the priority queue.
    Initialize a solution list.
    Use a second loop to pop off k values.
        - Everytime we pop off a value, we only append the coordinates (not the distance)

    Time Complexity: O(nlogn) because we have logn cost to push to heapq, and we do that n times.
        - After that, we pop off k times, with each pop being constant time.
        - Appending to the solution list is also constant time
    Space Complexity: O(n) because we store all of the lists.
        - I believe that we could get this down to O(k), since we know only need to store k values.
    """

    def kClosest(self, points, k):
        p_queue = []
        heapq.heapify(p_queue)
        # We only want to the p_queue to be of size k
        # We have to use a max heap of size k, so that we can pop off answers we know are not correct.
        # To implement a max heap, negate the values
        for x_coord, y_coord in points:
            distance = -1 * ((x_coord ** 2) + (y_coord ** 2))
            coord_info = (distance, (x_coord, y_coord))
            if len(p_queue) == k:
                # We don't want to just push, we want to push then pop, so that the size is the same
                heapq.heappushpop(p_queue, coord_info)
                # We don't need to do anything with the discarded value
            else:
                heapq.heappush(p_queue, coord_info)
        sol = []
        for _ in range(k):
            dist, coords = heapq.heappop(p_queue)
            sol.append(coords)
        return sol


if __name__ == '__main__':
    test_points = [[1, 3], [-2, 2]]
    test_k = 1
    solution_instance = Solution()
    print(solution_instance.kClosest(test_points, test_k))
