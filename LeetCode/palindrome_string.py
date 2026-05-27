s = "A man, a plan, a canal: Panama"

def is_palindrome(s: str) -> bool:
    clean = "".join(char for char in s if char.isalnum())
    clean = clean.lower()
    right = len(clean) - 1

    for i in clean:
        if i != clean[right]:
            return False
        right -= 1

    return True

print(f"is {s!r} a palindrome? : {is_palindrome(s)}")