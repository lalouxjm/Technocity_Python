s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

"""
def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        longest = max(longest, right - left + 1)

    return longest
"""


print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))