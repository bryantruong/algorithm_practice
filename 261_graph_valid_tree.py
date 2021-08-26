class Solution:
    """
    edges[i] = edges is a list of tuples [a, b], indicating an undirected edge between a and b
    Nodes are labeled from 0 to n-1
    Return if the edges of the graph make up the valid tree (T/F)
    The difference between a graph and a tree is that a graph can have cycles

    Solution: Use an adjacency list to build our graph.
    Keep a visiting set and a visited set
    Loop through each node in the dictionary. If the node has not been visited, yet:
    Do a DFS that keeps track of the parent
        Check if the currentt node is already in the visiting set. If so, false.
        In the DFS recursive routine, add the current node to the visiting set.
        Expand all of it's edges (not the parent one).
        Add the current node to visited (removing it from visiting)
        Return True

    Time complexity: O(V+E)
    An
    """

    def validTree(self, n: int, edges) -> bool:
        def dfs(curr_node, parent):
            """
            Helper function to perform DFS
            :return: Boolean (if we found a cycle)
            """
            if curr_node in seen:
                return False
            seen.add(curr_node)
            # Explore all its neighbors (except the parent)
            for neighbor in graph[curr_node]:
                # Don't revisit the parent, b/c it doesn't count as a cycle
                if parent is not None and parent == neighbor:
                    continue
                if not dfs(neighbor, curr_node):
                    return False
            return True

        # First, build the graph via adjacency list
        graph = {k: [] for k in range(n)}
        for node_1, node_2 in edges:
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)
        seen = set()
        # Should only have to call DFS once
        if not dfs(0, None):
            return False
        # Need to check that every node is reachable (the graph is connected)
        if len(seen) != n:
            return False
        return True


if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [0, 2], [1, 2]]
    solution_instance = Solution()
    print(solution_instance.validTree(n, edges))
