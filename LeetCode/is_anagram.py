s1 = "anagram"
s2 = "nagaram"

def is_anagram(s: str, t: str) -> bool:
    """
    if "".join(sorted(t)) == "".join(sorted(s)):
        return True
    return False
    """



print(f"is it an anagram? : {is_anagram(s1, s2)}")
