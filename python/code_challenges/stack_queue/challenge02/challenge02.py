from Stack import Stack

def isValid(s: str) -> bool:
    """
    Checks if the input string of brackets is valid. A string of brackets is considered valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    
    Args:
        s (str): The input string containing brackets.
    
    Returns:
        bool: True if the input string is valid, False otherwise.
    """
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            if stack.peek() == bracket_map[char]:
                stack.pop()
            else:
                return False

    return stack.is_empty()

# Test cases
print(isValid("()"))                 # Output: True
print(isValid("()[]{}"))             # Output: True
print(isValid("[({}]"))              # Output: False                            
print(isValid("[(hello)()]"))        # Output: True
print(isValid("[{(())}(){[]}]"))     # Output: True
print(isValid("{[((({{{{}}}})))]}")) # Output: True
