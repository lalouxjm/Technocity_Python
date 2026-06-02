from collections import Counter

str1 = "aaaabbbcdddd"
str2 = "abcd"
str3 = "abbcd"
str4 = "aa"

def char_counter(s: str):
    """
    temp = s[0]
    counter = 0
    result = []

    #for each character in the string
    for char in s:
        #if it's the same character we encountered before just count +1
        if temp == char:
            counter += 1
        #
        else:
            result.append(temp)
            result.append(str(counter))
            temp = char
            counter = 1
    result.append(temp)
    result.append(str(counter))

    compressed = "".join(result)

    return s if len(s) < len(compressed) else compressed
    """

print(char_counter(str1))
print(char_counter(str2))
print(char_counter(str3))
print(char_counter(str4))

def char_counter2(s: str):
    """
    counter = Counter(s)
    new_string = ""

    for i, v in counter.items():
        new_string += str(i)
        new_string += str(v)

    return s if len(s) < len(new_string) else new_string
    """


print(char_counter2(str1))
print(char_counter2(str2))
print(char_counter2(str3))
print(char_counter2(str4))