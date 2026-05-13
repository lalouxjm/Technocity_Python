test1 = "III"
test2 = "LVIII"
test3 = "MCMXCIV"

def roman_to_int(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0

    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]

    return result

print(roman_to_int(test1))
print(roman_to_int(test2))
print(roman_to_int(test3))