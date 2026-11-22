class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        adj = [[] for i in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        last = {}
        new_parent = parent[:]

        def dfs(node):
            ch = s[node]
            if ch in last:
                new_parent[node] = last[ch]

            old = last.get(ch)
            last[ch] = node

            for child in adj[node]:
                dfs(child)

            if old is None:
                del last[ch]
            else:
                last[ch] = old

        dfs(0)

        tree = [[] for i in range(n)]

        for i in range(1, n):
            tree[new_parent[i]].append(i)

        ans = [1] * n

        def calculate(node):
            for child in tree[node]:
                ans[node] += calculate(child)
            return ans[node]

        calculate(0)

        return ans