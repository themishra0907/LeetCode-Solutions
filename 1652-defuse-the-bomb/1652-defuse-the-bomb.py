class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        ans = []
        if k == 0:
            return [0] * n
        for i in range(n):
            s = 0
            if k > 0:
                for j in range(1, k + 1):
                    s += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    s += code[(i - j) % n]
            ans.append(s)
        return ans