class Solution:
    """
    3
    [[0,2],[1,2],[2,0]]
    starting_nodes = [False, True, False]
    traverse_graph(1)
    graph[1] = [2]
    traverse_graph[2]
        traverse_graph[0]

    """

    def findOrder(self, numCourses, prerequisites):
        # Rare base case
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        # First create the graph
        graph = {key: [] for key in range(numCourses)}
        starting_nodes = [True for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
            # Mark the prereq as false, since it has an in-edge
            starting_nodes[prereq] = False

        # Subroutine to traverse the graph and populate solution
        def traverse_graph(curr_node):
            if curr_node in visiting:
                return False
            visiting.add(curr_node)
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    if not traverse_graph(neighbor):
                        return False
            # Post order traversal
            visited.add(curr_node)
            solution.append(curr_node)
            return True

        visiting = set()
        visited = set()
        solution = []
        # Find the node that doesn't have any in-edges. We'll start our search from here.
        for course in graph:
            if starting_nodes[course]:
                # Start our traversal from here
                if not traverse_graph(course):
                    return []
        if len(solution) != numCourses:
            return []
        return solution


if __name__ == '__main__':
    solution_instance = Solution()
    numCourses = 8
    prerequisites = [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]]
    print(solution_instance.findOrder(numCourses, prerequisites))
