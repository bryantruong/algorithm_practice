from collections import defaultdict, deque


class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(set)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                # Draw the edge between current email and the first email for this account
                graph[email].add(account[1])
                graph[account[1]].add(email)
                email_to_name[email] = name
        # Now that the graph has been made, do DFS from each email
        # Only do it if that graph has not been visited yet

        visited = set()
        final_merged = []

        for email in graph:  # iterates through the keys in the graph dictionary
            # Do DFS if not visited yet
            if email not in visited:
                this_block = []
                to_expand = deque()
                # Start DFS from current email node
                to_expand.append(email)
                while to_expand:
                    curr_email = to_expand.pop()
                    visited.add(curr_email)
                    this_block.append(curr_email)
                    for neighbor in graph[curr_email]:
                        if neighbor not in to_expand and neighbor not in visited:
                            to_expand.append(neighbor)
                merged_account = [email_to_name[email], *sorted(this_block)]
                final_merged.append(merged_account)
        return final_merged


if __name__ == '__main__':
    test_case = [["David", "David0@m.co", "David1@m.co"],
                 ["David", "David3@m.co", "David4@m.co"],
                 ["David", "David4@m.co", "David5@m.co"],
                 ["David", "David2@m.co", "David3@m.co"],
                 ["David", "David1@m.co", "David2@m.co"]]
    solution_instance = Solution()
    print(solution_instance.accountsMerge(test_case))
