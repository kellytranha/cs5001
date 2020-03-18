from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    # Implement bracket matching functionality
    # as required by bracket_checker.py and by
    # bracket_match_test.py
    def __init__(self):
        self.bracket_pairs = {"(": ")", "[": "]", "{": "}"}

    def brackets_match(self, line):
        stack = Stack()

        for i in line:
            if i in self.bracket_pairs:
                stack.push(i)
            elif (stack.peek() is not None
                  and i == self.bracket_pairs.get(stack.peek())):
                stack.pop()
            elif (stack.peek() is None
                  and i in [")", "]", "}"]):
                return False
        return stack.peek() is None
