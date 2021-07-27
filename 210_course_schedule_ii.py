import bisect
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # First, create the graph.
        # My graph will have each node point to its prerequisites
        # <node, [prerequisites}>
        graph = {i: [] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            graph[course].append(pre_req)
        # Visited will be used
        solution = {}  # In python, sets do NOT maintain order, but dictionaries do
        visiting = set()

        # Use a inner function for dfs so that we can access these sets
        def dfs(node):
            # First add it to visiting set
            visiting.add(node)
            for neighbor in graph[node]:
                # This would indicate a cycle
                if neighbor in visiting:
                    return False
                # Only explore it if it hasn't been already explored
                if neighbor not in solution:
                    result = dfs(neighbor)
                    if not result:
                        return False
            # If all the neighbors (if any) are valid, then we can remove it from visiting and add it to solution
            visiting.remove(node)
            solution[node] = None
            return True

        for node in graph:
            if node not in solution:
                result = dfs(node)
                if not result:
                    return []
        return list(solution)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_num_courses = 2
    test_pre_reqs = [[0, 1]]
    solution_instance = Solution()
    print(solution_instance.findOrder(test_num_courses, test_pre_reqs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
