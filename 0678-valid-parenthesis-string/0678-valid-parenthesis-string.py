class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = 0
        for ch in s:
            if ch == '(':
                left += 1
                right += 1
            elif ch == ')':
                left -= 1
                right -= 1
            else:  # *
                left -= 1
                right += 1
            if right < 0:
                return False
                break
            left = max(left, 0)
        else:
            return (left == 0)