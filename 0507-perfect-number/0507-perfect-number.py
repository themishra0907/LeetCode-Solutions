class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        s = 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                s += i
                if i != num // i:
                    s += num // i

        return s == num