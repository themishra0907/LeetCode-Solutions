class Solution:
    def sumAndMultiply(self, n):
        x = 0
        digit_sum = 0
        place = 1

        while n > 0:
            digit = n % 10

            if digit != 0:
                x += digit * place
                digit_sum += digit
                place *= 10

            n //= 10

        return x * digit_sum