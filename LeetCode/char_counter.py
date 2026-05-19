s = "aaaabbbcdddd"

temp = s[0]
counter = 0
result = []

for char in s:
    if temp == char:
        counter += 1
    else:
            result.append(temp)
            result.append(str(counter))
            temp = char
            counter = 1
result.append(temp)
result.append(str(counter))

compressed = "".join(result)

print(s if len(s) < len(compressed) else compressed)