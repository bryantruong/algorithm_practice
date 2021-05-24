# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from collections import defaultdict


class Solution:
    # Below was my solution. Uses more space.
    # def findJudge(self, N: int, trust) -> int:
    #     # This is a quick way to tell if we should return -1:
    #     if len(trust) < N - 1:
    #         return -1
    #     # <node: {in_edges}, {out_edges}>
    #     graph_dict = defaultdict(lambda: (set(), set()))
    #     graph_dict[1] = set(), set()
    #     for relationship in trust:
    #         source_node = relationship[0]
    #         destination_node = relationship[1]
    #         # Add the out edge
    #         graph_dict[source_node][1].add(destination_node)
    #         graph_dict[destination_node][0].add(source_node)
    #     # Loop through the dictionary to check to see if they meet the criteria
    #     for node, edges in graph_dict.items():
    #         if len(edges[0]) == N-1 and len(edges[1]) == 0:
    #             return node
    #     return -1

    # Solution from LC
    def findJudge(self, N: int, trust) -> int:

        if len(trust) < N - 1:
            return -1

        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(1, N + 1):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i
        return -1

if __name__ == '__main__':
    solutionObject = Solution()
    answer = solutionObject.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
    print(answer)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
