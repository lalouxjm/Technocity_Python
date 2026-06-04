code1 = "12"
code2 = "226"
code3 = "06"
code4 = "100"
code5 = "117215421"

def decode_ways(code):
    if code[0] == "0":
        return 0

    ways = [0] * (len(code) + 1)
    ways[0] = ways[1] = 1

    for i in range(2, len(code)+1):
        one_way = int(code[i-1])
        two_ways = int(code[i-2:i])

        if 1 <= one_way <= 9:
            ways[i] += ways[i-1]
        if 10 <= two_ways <= 26:
            ways[i] += ways[i-2]
    return ways[len(code)]

print(decode_ways(code1))
print(decode_ways(code2))
print(decode_ways(code3))
print(decode_ways(code4))
print(decode_ways(code5))