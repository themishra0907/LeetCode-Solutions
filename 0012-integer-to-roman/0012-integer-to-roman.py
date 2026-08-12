class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # I - 1
        # V - 5
        # X - 10
        # L - 50
        # C - 100
        # D - 500
        # M - 1000
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        for value, symbol in roman_map:
            if num == 0:
                break
            count = num // value
            if count > 0:
                result.append(symbol * count)
                num %= value
        return "".join(result)

