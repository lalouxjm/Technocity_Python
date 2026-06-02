s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"
s5 = "([)]"

def is_valid(s: str) -> bool:
    """
    stack = []
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for v in s:
        if v in mapping.values():
            stack.append(v)
        else:
            if not stack:
                return False
            top = stack.pop()
            if top != mapping[v]:
                return False
    return len(stack) == 0
    """


print(is_valid(s1))
print(is_valid(s2))
print(is_valid(s3))
print(is_valid(s4))
print(is_valid(s5))
