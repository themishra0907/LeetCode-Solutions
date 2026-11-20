from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 1
        for x in nums:
            up = dp.get(x, 0) + 1
            same = dp.get(x - 1, 0) + 1
            dp[x + 1] = up
            dp[x] = same
            ans = max(ans, up, same)
        return ans