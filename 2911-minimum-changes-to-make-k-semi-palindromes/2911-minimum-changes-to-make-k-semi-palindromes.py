class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        for l in range(n):
            for r in range(l + 1, n):
                length = r - l + 1
                ans = float('inf')

                for d in range(1, length):
                    if length % d == 0:
                        changes = 0

                        for j in range(d):
                            a = l + j
                            b = r - (d - 1 - j) 
                            while a < b:
                                if s[a] != s[b]:
                                    changes += 1
                                a += d
                                b -= d

                        ans = min(ans, changes)

                cost[l][r] = ans

        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for i in range(1, k + 1):
            for j in range(2 * i, n + 1):
                for p in range(2 * (i - 1), j - 1):
                    dp[i][j] = min(dp[i][j], dp[i - 1][p] + cost[p][j - 1])

        return dp[k][n]