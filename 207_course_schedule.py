import bisect
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # Create a graph with key: int, value: the list of prerequisites needed to take before taking the class
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        # Graph is now built
        # This will only keep track of the current DFS visited nodes
        visited = set()

        def dfs(start_node):
            if start_node in visited:
                return False
            else:
                visited.add(start_node)
                for neighbor in graph[start_node]:
                    result = dfs(neighbor)
                    if not result:
                        return False
                # The key for a good time complexity is to not explore it if we know it is valid
                graph[start_node] = []
                visited.remove(start_node)
                return True

        # Now do DFS from each
        for key in list(graph):
            root_result = dfs(key)
            if not root_result:
                return False
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_num_courses = 5
    test_pre_reqs = [[1, 4], [2, 4], [3, 1], [3, 2]]
    solution_instance = Solution()
    print(solution_instance.canFinish(test_num_courses, test_pre_reqs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
