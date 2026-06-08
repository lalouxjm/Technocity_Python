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

a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(a.values())
print(a.keys())
print("".join(map(str,a.values())))
print("".join(a.keys()))
pref_bel = "+32"
p_number = "0493636120"
p_number_formatted = " ".join([
    pref_bel,
    p_number[1:4],
    p_number[4:6],
    p_number[6:8],
    p_number[8:],
])
print(p_number_formatted)