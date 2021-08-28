class Solution:
    """
    Treat this problem as an undirected graph problem.
    First create the graph via adjacency list. Then perform a DFS, putting each node into
    alternating groups. If we reach a node that has already been seen, check that it does not match
    the previously used group label. If it passes, return True. Otherwise, return false.

    Keep a visited dictionary that records each node and it's label.

    Solution:
    Have an outer for loop for each of the n people. If n is not in the visited dictionary, call
    the dfs subroutine. If it returns False, return False. Otherwise, after the for loop,
    return True.
       3
     /  \
    1  -  2

    1 -> 2 -> 4
    |
    v
    3
    """

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def separate_groups(curr_node, label):
            """
            curr_node = the integer representing the current node/person
            label = the integer that represents the label/group to assign
            """
            if curr_node in visited_dict:
                # Check to see if the existing label is valid.
                # This logic would work for undirected graph, but maybe not directed graph.
                if visited_dict[curr_node] != label:
                    return False
                return True
            # Mark the current node as visited and save the label
            visited_dict[curr_node] = label
            # Continue to explore/label each of the current node's neighbors
            for neighbor in graph[curr_node]:
                # Alternate labeling
                if not separate_groups(neighbor, -label):
                    return False
            return True

        visited_dict = {}
        graph = {k: [] for k in range(1, n + 1)}
        # Populate the graph by reading in the dislikes
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        for node in range(1, n + 1):
            if node not in visited_dict:
                if not separate_groups(node, 1):
                    return False
        return True

