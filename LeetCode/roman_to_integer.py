

test1 = "III"
test2 = "LVIII"
test3 = "MCMXCIV"


def roman_to_int(s):
    result = 0
    for i in range(len(s)-1):
        print(s[i], end=" ")
        if (s[i],(s[i+1])) == "CM":
            result -= 200
        if i == "M":
            result += 1000
        if i == "D":
            result += 500
        if i == "C":
            result += 100
        if i == "L":
            result += 50
        if i == "X":
            result += 10
        if i == "V":
            result += 5
        if i == "I":
            result += 1

    return result

print(roman_to_int(test1))
print(roman_to_int(test2))
print(roman_to_int(test3))