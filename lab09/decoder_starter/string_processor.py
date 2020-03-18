from stack import Stack


class StringProcessor:
    """Class for processing strings"""

    def process_string(self, line):
        stack = Stack()
        result = ""
        for i in line:
            if i == "*":
                to_be_added = stack.pop()
                if to_be_added is None:
                    continue
                result += to_be_added
            elif i == "^":
                first_char = stack.pop()
                if first_char is None:
                    continue
                result += first_char
                second_char = stack.pop()
                if second_char is None:
                    continue
                result += second_char
            else:
                stack.push(i)

        return result
