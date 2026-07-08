class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min(len(s) for s    in strs)
        i = 0
        while i<min_len:
            ch = strs[0][i]
            if all(s[i] == ch for s in strs):
                i+=1
            else:
                break
        return strs[0][:i]