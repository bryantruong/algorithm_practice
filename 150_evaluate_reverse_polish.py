from collections import deque


class Solution:
    """
    Evaluate the value of an expression in RPN, where operators follow their operands. 3 4 + in RPN equates to 3+4
        - Operators are given directly after the second operand.
        - Eliminates the need for parentheses
    Input is a list of tokens, for which we are supposed to process.
    Ex:
    ["2","1","+","3","*"] equates to (2 + 1) * 3 = 9
    Ex:
    ["4","13","5","/","+"] equates to 4 + (13// 5) = 6. This is because WE USE INTEGER DIVISION (13//5 = 2)

    Approach:
    Going to want to use a stack.
    Iterate through each token, add it to the stack.
    When we reach an operand:
        No need to add it to the stack,
        Pop off the previous two items from the stack.
        Perform the operation.
        Put the result back on the stack. Continue
    """

    def complete_operation(self, num_1, num_2, operator):
        """
        :param num_1, num_2: both char representtations of integers
        :param operator: a char representing the operation to perform
        :return: int
        """
        num_1 = int(num_1)
        num_2 = int(num_2)
        if operator == "+":
            return num_1 + num_2
        if operator == "-":
            return num_1 - num_2
        if operator == "*":
            return num_1 * num_2
        if operator == "/":
            # IMPORTANT! // always takes the floor. For rounding to zero, cast to int.
            return int(num_1/num_2)

    def evalRPN(self, tokens) -> int:
        stack = deque()
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                # We need to back up and take the last two elements from the stack
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                result = str(self.complete_operation(operand_1, operand_2, token))
                stack.append(result)
            else:
                stack.append(token)
        return stack.pop()


if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    solutionObject = Solution()
    print(solutionObject.evalRPN(tokens))
