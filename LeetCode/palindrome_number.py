test1 = 121
test2 = -121
test3 = 10

def is_palindrome(x: int) -> bool:
    y = str(x)
    left, right = 0, len(y) - 1

    while left < right:
        if y[left] == y[right]:
            return True
        else:
            left += 1
            right -= 1
    return False

print(is_palindrome(test1))
print(is_palindrome(test2))
print(is_palindrome(test3))