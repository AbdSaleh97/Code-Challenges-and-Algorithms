# Write your test here
from challenge02 import isValid
def test_valid_parentheses():
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("[({})]") == True
    assert isValid("[({}]") == False
    assert isValid("[{(())}]") == True
    assert isValid("{[()]}") == True
    assert isValid("{[(])}") == False
    assert isValid("{[}") == False
    assert isValid("{([])}") == True
    assert isValid("((()))") == True
    assert isValid("[[[]]]") == True
    assert isValid("{{{{}}}}") == True
    assert isValid("") == True
    assert isValid("(((((((((((())))))))))))") == True
    assert isValid("(((((((((((()))))))))))") == False