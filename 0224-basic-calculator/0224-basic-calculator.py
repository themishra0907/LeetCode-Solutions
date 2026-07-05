class Solution:
    def calculate(self, s):
        stack = []
        current_number = 0
        current_result = 0
        sign = 1  # 1 means positive (+), -1 means negative (-)

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char in '+-':
                # Commit the previous number to the result
                current_result += sign * current_number
                # Set the sign for the upcoming number
                sign = 1 if char == '+' else -1
                current_number = 0
            elif char == '(':
                # Save the current result and sign to the stack
                stack.append(current_result)
                stack.append(sign)
                # Reset for the expression inside the parentheses
                current_result = 0
                sign = 1
            elif char == ')':
                # Commit the last number inside the parentheses
                current_result += sign * current_number
                current_number = 0
                # Multiply by the sign outside the parenthesis, then add the old result
                current_result *= stack.pop()  # Saved sign
                current_result += stack.pop()  # Saved previous result
            # Spaces are naturally ignored because they don't match any condition

        # Catch the final number if the string doesn't end with a parenthesis
        return current_result + (sign * current_number)

        valu