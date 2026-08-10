import math
class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            # Check all possible square subtractions
            for k in range(1, int(math.sqrt(i)) + 1):
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # Found a winning move, no need to check further
                    
        return dp[n]