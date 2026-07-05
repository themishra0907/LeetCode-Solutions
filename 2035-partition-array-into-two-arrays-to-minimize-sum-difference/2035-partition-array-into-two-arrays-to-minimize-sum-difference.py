from bisect import bisect_left
class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums) // 2
        left = nums[:n]
        right = nums[n:]
        total = sum(nums)
        leftSum = [[] for _ in range(n + 1)]
        rightSum = [[] for _ in range(n + 1)]
        # generate all subset sums
        for mask in range(1 << n):
            cnt = 0
            s1 = 0
            s2 = 0
            for i in range(n):
                if mask & (1 << i):
                    cnt += 1
                    s1 += left[i]
                    s2 += right[i]
            leftSum[cnt].append(s1)
            rightSum[cnt].append(s2)
        # Sort right subset sums
        for i in range(n + 1):
            rightSum[i].sort()
        ans = float('inf')
        for k in range(n + 1):
            r = rightSum[n - k]
            for s1 in leftSum[k]:
                target = total / 2.0 - s1
                idx = bisect_left(r, target)
                if idx < len(r):
                    curr = s1 + r[idx]
                    ans = min(ans, abs(total - 2 * curr))
                if idx > 0:
                    curr = s1 + r[idx - 1]
                    ans = min(ans, abs(total - 2 * curr))
        return ans