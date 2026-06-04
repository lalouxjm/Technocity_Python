from collections import Counter

s = "abccccdd"

def longest_palindrome(s):
    """
    counts = Counter(s)
    longest = 0
    odds = False

    for count in counts.values():
        if count % 2 == 1:
            odds = True

        longest += (c//2)*2

    if odds:
        longest += 1

    return longest
    """


print(longest_palindrome(s))