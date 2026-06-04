from collections import Counter


ransomNote1 = "a"
magazine1 = "b"
ransomNote2 = "aa"
magazine2 = "ab"
ransomNote3 = "aa"
magazine3 = "aab"


def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom = Counter(ransomNote)
    mag = Counter(magazine)

    for char in ransom:
        if ransom[char] > mag[char]:
            return False
    return True

print(canConstruct(ransomNote1, magazine1))
print(canConstruct(ransomNote2, magazine2))
print(canConstruct(ransomNote3, magazine3))